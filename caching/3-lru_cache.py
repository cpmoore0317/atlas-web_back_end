#!/usr/bin/env python3
"""3-lru_caching.py"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements a
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
        Initializes the LRUCache instance.
        Calls the parent class BaseCaching's __init__ method.
        """
        super().__init__()
        self.lru_queue = []  # Queue to track the order of recently used keys

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using LRU eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache is full, evicts the least recently used item (LRU).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_lru_queue(key)  # Update the LRU queue

            if len(self.cache_data) > self.MAX_ITEMS:
                # Evict the least recently used item (LRU)
                lru_key = self.lru_queue.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            self.update_lru_queue(key)  # Update the LRU queue
            return self.cache_data[key]
        return None

    def update_lru_queue(self, key):
        """
        Updates the LRU queue with the given key.

        Args:
            key: The key to update in the LRU queue.
        """
        if key in self.lru_queue:
            self.lru_queue.remove(key)  # Remove existing occurrence
        self.lru_queue.append(key)  # Add the key to the end of the queue
