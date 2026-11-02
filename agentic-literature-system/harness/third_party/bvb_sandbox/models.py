"""Model access via litellm.

litellm routes by model name (e.g. ``gpt-6-astra``, ``anthropic/claude-sonnet-4.6``,
``gemini/gemini-2.5-pro``), handles retries/rate-limits internally, and ships a
price database so the per-call USD cost is computed for us -- no hand-maintained
prices. Cost is the single budget lever (mini-swe-agent style).

Neutral message format (provider-agnostic):
    message = {"role": "user"|"assistant", "parts": [part, ...]}
    part    = {"kind": "text", "text": str}
            | {"kind": "image", "data": <base64>, "media_type": "image/jpeg"}
"""

from __future__ import annotations

from typing import Any

import os
import math
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
import litellm


def text_part(text: str) -> dict[str, Any]:
    return {"kind": "text", "text": text}


def image_part(data_b64: str, media_type: str = "image/jpeg") -> dict[str, Any]:
    return {"kind": "image", "data": data_b64, "media_type": media_type}


def _content(parts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for part in parts:
        if part["kind"] == "text":
            out.append({"type": "text", "text": part["text"]})
        else:
            url = f"data:{part['media_type']};base64,{part['data']}"
            out.append({"type": "image_url", "image_url": {"url": url}})
    return out


def _usage_value(usage: Any, name: str) -> int:
    if usage is None:
        return 0
    if isinstance(usage, dict):
        return int(usage.get(name, 0) or 0)
    return int(getattr(usage, name, 0) or 0)


def _manual_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Fallback for routes where litellm.completion_cost returns 0.

    Some hosted routes (notably a few OpenRouter models) have prices in
    litellm.model_cost but completion_cost does not attach them to the response.
    Use the same litellm price database directly so cost_limit remains the only
    budget lever.
    """
    configured = [os.environ.get(key) for key in ("INPUT_COST_PER_MILLION", "OUTPUT_COST_PER_MILLION")]
    if any(value is not None for value in configured):
        try:
            rates = [float(value) for value in configured]
        except (TypeError, ValueError):
            raise ValueError("Set both INPUT_COST_PER_MILLION and OUTPUT_COST_PER_MILLION to nonnegative USD rates") from None
        if any(not math.isfinite(rate) or rate < 0 for rate in rates) or not any(rates):
            raise ValueError("Cost rates must be finite, nonnegative, and not both zero")
        return (input_tokens * rates[0] + output_tokens * rates[1]) / 1_000_000
    candidates = [model, model.split("/")[-1]]
    for key in candidates:
        price = litellm.model_cost.get(key)
        if not price:
            continue
        input_price = float(price.get("input_cost_per_token") or 0.0)
        output_price = float(price.get("output_cost_per_token") or 0.0)
        if input_price or output_price:
            return input_tokens * input_price + output_tokens * output_price
    if input_tokens or output_tokens:
        raise ValueError("Unknown model pricing; configure INPUT_COST_PER_MILLION and OUTPUT_COST_PER_MILLION")
    return 0.0


class Model:
    def __init__(
        self,
        model: str,
        *,
        reasoning: str | None = None,
        timeout: float = 600.0,
        num_retries: int = 5,
    ) -> None:
        self.model = model
        self.name = model
        self.reasoning = reasoning
        self.timeout = timeout
        self.num_retries = num_retries

    def complete(self, system: str, messages: list[dict[str, Any]]) -> tuple[str, dict[str, Any]]:
        """Return (text, info) where info = {cost, input_tokens, output_tokens}."""
        oai_messages = [{"role": "system", "content": system}]
        oai_messages += [{"role": m["role"], "content": _content(m["parts"])} for m in messages]
        kwargs: dict[str, Any] = {}
        if self.reasoning:
            # LiteLLM maps this to provider-native reasoning/thinking settings:
            # OpenAI reasoning_effort, Anthropic adaptive thinking/output_config,
            # Gemini thinking budget, etc.
            kwargs["reasoning_effort"] = self.reasoning
            # LiteLLM 1.99 has Astra's capability/price metadata but its OpenAI
            # parameter allowlist predates GPT-6. Forward the official parameter
            # explicitly; newer LiteLLM versions accept this harmlessly too.
            if self.model.lower() in {"gpt-6-astra", "openai/gpt-6-astra"}:
                kwargs["allowed_openai_params"] = ["reasoning_effort"]
        response = litellm.completion(
            model=self.model,
            messages=oai_messages,
            timeout=self.timeout,
            num_retries=self.num_retries,
            **kwargs,
        )
        text = response.choices[0].message.content or ""
        usage = getattr(response, "usage", None)
        input_tokens = _usage_value(usage, "prompt_tokens")
        output_tokens = _usage_value(usage, "completion_tokens")
        try:
            cost = float(litellm.completion_cost(completion_response=response) or 0.0)
        except Exception:
            cost = 0.0
        if cost == 0.0 and (input_tokens or output_tokens):
            cost = _manual_cost(self.model, input_tokens, output_tokens)
        return text, {
            "cost": cost,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        }
