#!/usr/bin/python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Use the self.cache_data, put and get method from BaseCaching class"""
    def put(self, key, item):
        """assign to the dictionary the item as value and key as key"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve item from the dictionary"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
