#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
from time import perf_counter

async_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function that execute async_comprehesion four times in parallel
       using asyncio.gather"""
    start = perf_counter()
    await asyncio.gather(*(async_comp() for _ in range(4)))
    return perf_counter() - start
