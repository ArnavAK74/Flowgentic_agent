# agent_core/simple_pipeline.py

import os
import json
from impress.pipelines.impress_pipeline import ImpressBasePipeline


class SimpleProteinPipeline(ImpressBasePipeline):
    """
    Phase-2 placeholder IMPRESS pipeline.
    Writes results to:
        <workspace>/results/output.json
    Pipeline receives workspace path via kwargs from executor.
    """

    def register_pipeline_tasks(self):
        """
        Required by ImpressBasePipeline.
        No distributed tasks needed in Phase 2.
        """
        pass

    async def run(self):
        """
        Execute the pipeline.
        Save a deterministic output JSON to the workspace.
        """

        print("[SimplePipeline] Running Phase 2 placeholder pipeline...")

        # All inputs provided via PipelineSetup appear in self.config
        inputs = self.config

        # Workspace must be provided by executor
        workspace = inputs.get("workspace")
        if not workspace:
            raise ValueError(
                "Pipeline did not receive 'workspace' in kwargs. "
                "Executor must pass workspace path."
            )

        # Create results directory
        results_dir = os.path.join(workspace, "results")
        os.makedirs(results_dir, exist_ok=True)

        # Dummy output (Phase 2)
        result = {
            "message": "Simple IMPRESS pipeline completed successfully.",
            "inputs": inputs,
            "output_stub": {
                "structure": "PDB_STUB",
                "homologs": ["1abcA", "4xyzB"],
                "ddg": {"A10V": 1.2},
            }
        }

        # Save output.json
        output_path = os.path.join(results_dir, "output.json")

        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)

        print(f"[SimplePipeline] Saved results to: {output_path}")

        # Store output path in internal state (optional)
        self.state["output_path"] = output_path

        return result

    async def finalize(self):
        """
        Optional cleanup step required by ImpressBasePipeline.
        """
        print("[SimplePipeline] Finalizing (no-op).")
        return {}

