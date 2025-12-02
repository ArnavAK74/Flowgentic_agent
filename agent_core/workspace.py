# agent_core/workspace.py

import os
from pathlib import Path
import time

# NEW BASE PATH
BASE = "/home/x-akumar42/flowgentic_agent/agent_workspace"

class WorkspaceManager:

    def create(self) -> str:
        ts = int(time.time())
        wdir = Path(BASE) / f"Q_{ts}"

        (wdir / "input").mkdir(parents=True, exist_ok=True)
        (wdir / "logs").mkdir(parents=True, exist_ok=True)
        (wdir / "results").mkdir(parents=True, exist_ok=True)
        (wdir / "intermediate").mkdir(parents=True, exist_ok=True)

        return str(wdir)

