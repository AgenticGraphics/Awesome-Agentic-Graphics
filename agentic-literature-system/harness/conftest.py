"""Keep offline tests independent of live model pricing services."""
import os
os.environ["LITELLM_LOCAL_MODEL_COST_MAP"] = "True"
