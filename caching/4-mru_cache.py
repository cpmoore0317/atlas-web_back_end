#!/usr/bin/env python3
"""4-mru_caching.py"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements a
    caching system.

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
        Initializes the MRUCache instance.
        Calls the parent class BaseCaching's __init__ method.
        """
        super().__init__()
        self.mru_queue = []  # Queue to track the order of recently used keys

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using MRU eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache is full, evicts the most recently used item (MRU).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_mru_queue(key)  # Update the MRU queue

            if len(self.cache_data) > self.MAX_ITEMS:
                # Evict the most recently used item (MRU)
                mru_key = self.mru_queue.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            self.update_mru_queue(key)  # Update the MRU queue
            return self.cache_data[key]
        return None

    def update_mru_queue(self, key):
        """
        Updates the MRU queue with the given key.

        Args:
            key: The key to update in the MRU queue.
        """
        if key in self.mru_queue:
            self.mru_queue.remove(key)  # Remove existing occurrence
        self.mru_queue.append(key)  # Add the key to the end of the queue
