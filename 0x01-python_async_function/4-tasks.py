#!/usr/bin/env python3
"""Call task_wait_n function in task_wait_random function"""
from asyncio import as_completed
from typing import List

twr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    y = [twr(max_delay) for _ in range(n)]
    return [await task for task in as_completed(y)]
