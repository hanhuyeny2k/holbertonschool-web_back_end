#!/usr/bin/env python3
"""The basics of async"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """wait for random delay between 0 and 10 seconds and return it"""
    y = uniform(0, max_delay)
    await asyncio.sleep(y)
    return y
