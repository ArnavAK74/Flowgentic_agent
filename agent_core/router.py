# agent_core/router.py

import re
from typing import Dict, Any

class Router:

    def route(self, prompt: str) -> Dict[str, Any]:
        prompt = prompt.lower()

        if "predict structure" in prompt and "homolog" in prompt:
            return {
                "pipeline": "protein_binding",
                "intent": "structure+homolog_search",
            }

        if "predict structure" in prompt:
            return {"pipeline": "protein_binding", "intent": "structure_only"}

        if "ddg" in prompt or "mutation" in prompt:
            return {"pipeline": "protein_binding", "intent": "ddg_only"}

        return {"pipeline": "protein_binding", "intent": "generic"}

