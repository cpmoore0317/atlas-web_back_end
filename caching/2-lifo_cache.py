#!/usr/bin/env python3
"""2-lifo_caching.py"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a caching system.

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
        Initializes the LIFOCache instance.
        Calls the parent class BaseCaching's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using LIFO eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache is full, evicts the last item added (LIFO).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                # Evict the last item added (LIFO)
                last_key = self.get_last_key()
                if last_key:
                    print(f"DISCARD: {last_key}")
                    del self.cache_data[last_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)

    def get_last_key(self):
        """
        Gets the key of the last item added to the cache (LIFO).

        Returns:
            The key of the last item, or None if the cache is empty.
        """
        if self.cache_data:
            return next(reversed(self.cache_data))
        return None

# Example usage
if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
AI-generated code. Review and use carefully. More info on FAQ.
When you run the provided example (2-main.py), it will demonstrate the LIFO behavior of the cache. Feel free to adapt this class for your specific use case! 😊

Learn more

1

github.com
2

github.com
3

github.com


You
I get the error that a dict object is not reversible
Copilot
I apologize for the oversight. You’re right; Python dictionaries are not inherently reversible. Let’s address this issue in the LIFOCache class.

To fix the error, we’ll convert the dict_keys object (which is not reversible) to a list before using it in the reversed() function. Here’s the updated implementation:

Python

class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements a caching system.

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
        Initializes the LIFOCache instance.
        Calls the parent class BaseCaching's __init__ method.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns the item value to the key in the cache using LIFO eviction.

        Args:
            key: The key for the cache entry.
            item: The value to be stored in the cache.

        Notes:
            If key or item is None, this method does nothing.
            If the cache is full, evicts the last item added (LIFO).
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                # Convert dict_keys to a list and get the last key (LIFO)
                last_key = self.get_last_key()
                if last_key:
                    print(f"DISCARD: {last_key}")
                    del self.cache_data[last_key]

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value linked to the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)

    def get_last_key(self):
        """
        Gets the key of the last item added to the cache (LIFO).

        Returns:
            The key of the last item, or None if the cache is empty.
        """
        if self.cache_data:
            return next(reversed(list(self.cache_data.keys())))
        return None
