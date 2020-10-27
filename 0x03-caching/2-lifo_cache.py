#!/usr/bin/python3
""" Get and retrieve items using LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """add data to the cache"""
        if key is None or item is None:
            return
        if key in self.keys:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.keys.pop()
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve data from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
