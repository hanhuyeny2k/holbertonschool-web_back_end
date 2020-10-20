#!/usr/bin/env python3
"""Type-annotated to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple with string and the square of an int and/or float"""
    return (k, v**2)
