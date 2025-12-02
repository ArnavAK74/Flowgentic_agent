# tools/ddg_stub.py

import asyncio

async def run(params, workspace):
    await asyncio.sleep(1)
    return {"ddg_values": {"A10V": 1.2, "L50F": -0.8}}

