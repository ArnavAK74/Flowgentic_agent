# agent_core/models.py

from dataclasses import dataclass, field
from typing import Dict, Any, List
import uuid
import time

@dataclass
class WorkflowStep:
    """Single stage in a pipeline (AF2, FoldSeek, etc.)"""
    name: str
    params: Dict[str, Any]
    tool: str               # maps to tools/ or pipelines/
    step_id: str = field(default_factory=lambda: f"step_{uuid.uuid4().hex[:8]}")

@dataclass
class WorkflowPlan:
    """Full workflow planned from natural-language prompt."""
    workflow_id: str = field(default_factory=lambda: f"Q_{int(time.time())}")
    steps: List[WorkflowStep] = field(default_factory=list)
    user_prompt: str = ""
    workspace_dir: str = ""

    def add_step(self, name: str, tool: str, params: Dict[str, Any]):
        self.steps.append(WorkflowStep(name=name, tool=tool, params=params))

