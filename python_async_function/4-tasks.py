#!/usr/bin/env python3
"""4-tasks.py"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns n instances of task_wait_random with the
    specified max_delay. Returns a list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(tasks)
    delays = [task.result() for task in completed_tasks]
    return sorted(delays)
