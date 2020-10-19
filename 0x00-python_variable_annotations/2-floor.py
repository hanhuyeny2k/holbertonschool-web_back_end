#!/usr/bin/env python3
"""Type-annotated floor function"""


def floor(n: float) -> int:
    """return the floor of the float"""
    if n < 0 and n != int(n):
        return int(n + 1)
    return int(n)
