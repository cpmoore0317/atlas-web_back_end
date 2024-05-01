#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random


async def async_generator():
    """An asynchronous generator that yields random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
