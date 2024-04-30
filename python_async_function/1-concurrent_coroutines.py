#!/usr/bin/env python3
"""
Module that imports wait_random to create an async routine that takes 2 int arguments.
wait_random spawns n times with the specified max_delay.
"""
__import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns n wait_random coroutines with the specifies max_delay
    and returns a list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
