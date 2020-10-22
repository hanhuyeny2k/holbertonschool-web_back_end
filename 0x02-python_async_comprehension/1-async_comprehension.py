#!/usr/bin/env python3
"""Async comprehensions"""
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    "using async comprehension to return 10 random numbers"""
    y = [rand async for rand in async_gen()]
    return y
