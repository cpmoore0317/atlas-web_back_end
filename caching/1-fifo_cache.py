#!/usr/bin/env python3
"""1-fifo_caching.py"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system that uses the First-In-First-Out (FIFO) algorithm.

    Inherits from BaseCaching.

    Attributes:
        cache_data (dict): Dictionary to store cached data.

    Methods:
        put(key, item):
            Adds an item to the cache.
            Args:
                key: The key for the cache entry.
                item: The value to be stored in the cache.

        get(key):
            Retrieves the value associated with the given key from the cache.
            Args:
                key: The key to look up in the cache.
            Returns:
                The value linked to the key, or None if the key doesn't exist.
    """
    def __init__(self):
        """
        Initializes the FIFOCache instance.
        Calls the parent class BaseCaching's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using FIFO eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache is full, evicts the first item added (FIFO).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                # Evict the first item added (FIFO)
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
