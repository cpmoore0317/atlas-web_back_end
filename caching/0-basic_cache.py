#!/usr/bin/env python3
"""0-basic_cache.py"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Assigns the item value to the key in the cache.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
