#!/usr/bin/env python3


"""
a class MRU cache that inherits from BaseCaching and is a caching system
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A Cache that uses the least recently used
    algorithm to cache data
    """

    track_record = {}

    def add_key_to_track_record(self, key):
        """Adds item to the tract record data structure"""
        if len(self.track_record) == 0:
            self.track_record[key] = 0
        else:
            values = list(self.track_record.values())
            last_value = values[len(values) - 1]
            self.track_record[key] = last_value + 1

    def set_track_record_with_replacement(self, new_key):
        """Update the track record data structure when a replacement
        occurs
        """
        key_to_pop = None
        highest_value_in_track_record = list(self.track_record.values())[0]
        
        for value in list(self.track_record.values()):
            if value > highest_value_in_track_record:
                highest_value_in_track_record = value

        for key, item in self.track_record.items():
            if item == highest_value_in_track_record:
                key_to_pop = key
        self.track_record.pop(key_to_pop)
        self.cache_data.pop(key_to_pop)
        print(f"DISCARD: {key_to_pop}")
        # for key, item in self.track_record.items():
        #     if item <= self.MAX_ITEMS - 1 and item != 0:
        #         self.track_record[key] -= 1
        self.track_record[new_key] = self.MAX_ITEMS - 1

    def set_track_record_with_retrieval(self, old_key):
        """update the track record data structure when a retrieval
        occurs
        """
        highest_value_in_track_record = list(self.track_record.values())[0]
        for key, item in self.track_record.items():
            if item > highest_value_in_track_record:
                highest_value_in_track_record = item
        self.track_record[old_key] = highest_value_in_track_record

    def put(self, key, item):
        """Stores data into the cache
        """
        if key is None or item is None:
            return
        if len(self.track_record) < self.MAX_ITEMS:
            if key not in self.cache_data:
                self.add_key_to_track_record(key)
                self.cache_data[key] = item
            else:
                self.set_track_record_with_retrieval(key)
                self.cache_data[key] = item
        else:
            if key not in self.cache_data:
                self.set_track_record_with_replacement(key)
                self.cache_data[key] = item
            else:
                self.set_track_record_with_retrieval(key)
                self.cache_data[key] = item

    def get(self, key):
        """retrieve data stored in the cache"""
        if key is None:
            return None
        if key in self.cache_data:
            self.set_track_record_with_retrieval(key)
            return self.cache_data.get(key)
        return None
