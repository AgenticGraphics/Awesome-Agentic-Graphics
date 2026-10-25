"""Configuration comes from the caller, never from a developer machine."""
import os
from urllib.parse import urlparse


def api_base():
    value = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError("OPENAI_BASE_URL must be an HTTP(S) API root without credentials, query, or fragment")
    return value


def api_key():
    value = os.environ.get("OPENAI_API_KEY", "").strip()
    if not value:
        raise ValueError("Set OPENAI_API_KEY in your environment before a live run")
    return value


def model_name(value=None):
    value = value or os.environ.get("AGENT_MODEL", "").strip()
    if not value or value == "YOUR_MODEL_ID":
        raise ValueError("Select an available model with --model or AGENT_MODEL")
    return value


def search_model():
    return os.environ.get("SEARCH_MODEL", "").strip() or model_name()
