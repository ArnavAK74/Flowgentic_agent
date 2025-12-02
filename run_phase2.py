# run_phase2.py

import asyncio
from agent_core.executor import ImpressExecutor
from agent_core.workspace import WorkspaceManager


async def main():

    print("=== FlowGentic-IMPRESS Agent – Phase 2 ===")
    pipeline_name = input("Enter pipeline name (e.g., simple_pipeline): ").strip()

    fasta = input("Paste FASTA (or press Enter to skip): ").strip()
    kwargs = {}
    if fasta:
        kwargs["fasta"] = fasta

    # Create workspace
    ws = WorkspaceManager()
    workspace = ws.create()

    print(f"[Agent] Workspace created at: {workspace}")
    print("[Running pipeline...]\n")

    # Run IMPRESS pipeline
    executor = ImpressExecutor()
    result = await executor.execute(
        pipeline_name=pipeline_name,
        workspace=workspace,
        pipeline_kwargs=kwargs
    )

    print("\n=== FINAL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())

