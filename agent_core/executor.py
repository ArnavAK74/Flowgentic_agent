# agent_core/executor.py

import asyncio
import os
import json
from typing import Any, Dict

from radical.asyncflow import WorkflowEngine
from radical.asyncflow.backends.execution.radical_pilot import RadicalExecutionBackend

from impress.impress_manager import ImpressManager
from impress.pipelines.setup import PipelineSetup

from agent_core.simple_pipeline import SimpleProteinPipeline


class ImpressExecutor:
    """
    Executor for running IMPRESS pipelines using Radical Pilot backend.
    Compatible with YOUR IMPRESS VERSION, which uses:
        - WorkflowEngine(backend=...)
        - submit_new_pipelines()
        - start(pipeline_setups)
    """

    def __init__(self, backend_config: Dict[str, Any] | None = None):

        # Defaults (can be overridden for GPU jobs)
        self.backend_config = backend_config or {
            "resource": "purdue.anvil",
            "cores": 4,
            "gpus": 0,
            "runtime": 30,  # minutes
        }

        self.backend = None
        self.manager = None
        self.flow = None  # must be created manually for your IMPRESS version

    # ---------------------------------------------------------------------
    # Initialize backend + WorkflowEngine + IMPRESS Manager
    # ---------------------------------------------------------------------
    async def _init_backend(self):
        print("[Executor] Initializing RadicalExecutionBackend (await)...")

        # Must be awaited (starts RP agents)
        self.backend = await RadicalExecutionBackend(self.backend_config)
        print("[Executor] Backend initialized.")

        # Your WorkflowEngine requires backend argument!
        self.flow = WorkflowEngine(backend=self.backend)

        # Create ImpressManager
        self.manager = ImpressManager(execution_backend=self.backend)

        # Attach flow (required by submit_new_pipelines())
        self.manager.flow = self.flow

    # ---------------------------------------------------------------------
    # Main execution method
    # ---------------------------------------------------------------------
    async def execute(self, pipeline_name: str, workspace: str, pipeline_kwargs: dict | None = None):

        print(f"[Executor] Launching pipeline: {pipeline_name}")

        await self._init_backend()

        # Ensure workspace is passed into pipeline config
        pipeline_kwargs = pipeline_kwargs or {}
        pipeline_kwargs["workspace"] = workspace

        # Build pipeline setup
        setup = PipelineSetup(
            name=pipeline_name,
            type=SimpleProteinPipeline,
            config={},                     # no config overrides yet
            adaptive_fn=None,              # Phase 3
            kwargs=pipeline_kwargs,        # includes FASTA, workspace, etc.
        )

        try:
            print("[Executor] Submitting pipeline to IMPRESS...")
            self.manager.submit_new_pipelines([setup])

            print("[Executor] Starting IMPRESS Manager...")
            await self.manager.start([setup])

            print("[Executor] Pipeline completed.")

        except Exception as e:
            print(f"[Executor] Pipeline FAILED: {e}")
            return {"status": "error", "error": str(e)}

        # ------------------------------------------------------------------
        # Load results saved by pipeline (output.json)
        # ------------------------------------------------------------------
        result_path = os.path.join(workspace, "results", "output.json")

        if os.path.exists(result_path):
            with open(result_path, "r") as f:
                result_json = json.load(f)
        else:
            result_json = {
                "warning": "Pipeline did not write output.json",
                "checked_path": result_path
            }

        # ------------------------------------------------------------------
        # Backend shutdown (skip; your backend has no close())
        # ------------------------------------------------------------------
        print("[Executor] Backend shutdown skipped (no close() method).")

        # ------------------------------------------------------------------
        # Return final structured result
        # ------------------------------------------------------------------
        return {
            "status": "success",
            "pipeline": pipeline_name,
            "workspace": workspace,
            "result": result_json
        }

