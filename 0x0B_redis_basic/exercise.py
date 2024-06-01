#!/usr/bin/env python3
"""
This module contains the Cache class which provides methods to interact with Redis,
and decorators for counting method calls and storing call history.
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to increment the count for the method call and then
        call the original method.

        Args:
            self: The instance of the class.
            *args: The positional arguments for the method.
            **kwargs: The keyword arguments for the method.

        Returns:
            The return value of the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to store the input and output history of the method call.

        Args:
            self: The instance of the class.
            *args: The positional arguments for the method.
            **kwargs: The keyword arguments for the method.

        Returns:
            The return value of the original method.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


class Cache:
    """
    Cache class to interact with Redis for storing and retrieving data.
    """

    def __init__(self):
        """
        Initialize a Cache instance with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data stored at the given key in Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve data from Redis.
            fn (Optional[Callable]): A function to convert the data back to the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data in the appropriate format, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data stored at the given key in Redis and convert it to a string.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            Optional[str]: The retrieved data as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data stored at the given key in Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            Optional[int]: The retrieved data as an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
