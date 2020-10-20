#!/usr/bin/env python3
"""Type-annotated make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function that mutiplies a float by multiplier"""
    return lambda mul: mul * multiplier
