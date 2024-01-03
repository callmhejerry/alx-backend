#!/usr/bin/env python3


"""
a class Fifo cache that inherits from BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A Cache that acts in the First in
    first out manner
    """

    def put(self, key, item):
        """Stores data into the cache using the FIFO
        manner
        """
        if key is None or item is None:
            return
        keys = list(self.cache_data.keys())
        if len(self.cache_data) == self.MAX_ITEMS and key not in keys:
            keys = list(self.cache_data.keys())
            print(f"DISCARD: {keys[0]}")
            self.cache_data.pop(keys[0])
        self.cache_data[key] = item

    def get(self, key):
        """retrieve data stored in the cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
