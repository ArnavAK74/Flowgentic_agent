# agent_core/planner.py

from agent_core.models import WorkflowPlan
from agent_core.router import Router
from agent_core.workspace import WorkspaceManager

class Planner:

    def __init__(self):
        self.router = Router()
        self.ws = WorkspaceManager()

    def plan(self, prompt: str) -> WorkflowPlan:
        route = self.router.route(prompt)
        wp = WorkflowPlan(user_prompt=prompt)

        # Create workspace
        wp.workspace_dir = self.ws.create()

        intent = route["intent"]

        if intent in ("structure_only", "structure+homolog_search", "generic"):
            wp.add_step(
                "predict_structure",
                tool="alphafold_stub",
                params={"fasta": self._extract_fasta(prompt)}
            )

        if intent in ("structure+homolog_search", "generic"):
            wp.add_step(
                "foldseek_search",
                tool="foldseek_stub",
                params={}
            )

        if "ddg" in prompt or "mutation" in prompt or intent == "generic":
            wp.add_step(
                "ddg_mutation",
                tool="ddg_stub",
                params={"mutations": self._extract_mutations(prompt)}
            )

        return wp

    def _extract_fasta(self, prompt: str):
        if ">" in prompt:
            return prompt.split(">", 1)[1].strip()
        return "FASTA_NOT_PROVIDED"

    def _extract_mutations(self, prompt: str):
        return ["A10V", "L50F"]

