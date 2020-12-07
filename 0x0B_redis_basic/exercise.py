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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data stored at a key"""
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """get a string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get an int"""
        return self.get(key, int)


def count_calls(method: Callable) -> Callable:
    """Count calls of Cache methods"""
    qualname = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(qualname)
        return method(self, *args, **kwargs)
    return wrapper
