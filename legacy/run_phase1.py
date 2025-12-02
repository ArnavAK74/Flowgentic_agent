import asyncio
from agent_core import FlowPlanner, ImpressExecutor

async def main():

    print("=== Phase 1: FlowGentic-IMPRESS Executor ===")

    planner = FlowPlanner()
    workflow = planner.plan()
    print(f"[Planner] Planned workflow: {workflow}")

    executor = ImpressExecutor()

    # call async method properly
    await executor.execute("protein_binding")


if __name__ == "__main__":
    asyncio.run(main())

