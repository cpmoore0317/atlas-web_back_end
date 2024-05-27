#!/usr/bin/env python3
"""4-mru_caching.py"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching system """

    def __init__(self):
        """ Initializes MRUCache """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ Saves item in the cache, discards the most
        recently used item if limit exceeded """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru = self.access_order.pop()
                del self.cache_data[mru]
                print("DISCARD:", mru)

            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ Retrieves item by key, updates its access as most recent """
        if key is not None and key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
