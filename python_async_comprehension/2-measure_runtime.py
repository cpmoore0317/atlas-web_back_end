#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
