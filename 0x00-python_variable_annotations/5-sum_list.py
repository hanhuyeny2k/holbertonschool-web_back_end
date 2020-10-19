#!/usr/bin/env python3
"""Type-annotated sum_list function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of a list as a float"""
    return sum(input_list)
