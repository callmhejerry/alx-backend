#!/usr/bin/env python3


"""
a class BasicCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic Cache class
    """
    
    def put(self, key, item):
        """stores data to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieve data from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)