#!/usr/bin/env python3
"""Annotate the following function's parameters"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return values with the appropriate type"""
    return [(i, len(i)) for i in lst]
