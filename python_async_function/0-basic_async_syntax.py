#!/usr/bin/env python3
"""
Module for an anschronous coroutine that waits for a random delay,
then returns the random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay, then returns the random delay as a float.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
