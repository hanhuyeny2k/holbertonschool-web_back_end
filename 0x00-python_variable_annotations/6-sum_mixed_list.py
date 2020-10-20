#!/usr/bin/env python3
"""Type-annotated sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """return the sum of mixed list as a float"""
    return sum(mxd_lst)
