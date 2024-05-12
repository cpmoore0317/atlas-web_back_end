#!/usr/bin/env python3
"""2-lifo_caching.py"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a caching system.
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance.
        """
        super().__init__()
        self.key_order = []  # Maintain order of keys

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using LIFO eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.key_order.append(key)  # Add key to order
            if len(self.cache_data) > self.MAX_ITEMS:
                # Pop the last added key (LIFO)
                last_key = self.key_order.pop(0)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
