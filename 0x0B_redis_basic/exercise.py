#!/usr/bin/env python3
"""Redis Caching"""
from functools import wraps
from typing import Callable, Optional, Union
from uuid import uuid4
from redis.client import Redis


class Cache:
    """Redis Cache"""

    def __init__(self):
        """Redis cache wrapper"""
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a key, store data at it and return it"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
