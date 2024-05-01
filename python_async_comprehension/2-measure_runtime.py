#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async
    comprehension over async_generator.
    """
    result = [i async for i in async_generator()]
    return result


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension()
        async_comprehension()
        async_comprehension()
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
