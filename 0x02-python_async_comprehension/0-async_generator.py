#!/usr/bin/env python3
"""Async generator"""
from random import uniform
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times and in each asynchronously wait 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
