#!/usr/bin/env python3
"""
Module for taking a mixed set of types and returning a tuple.
"""
from typing import Union


def to_kv(k: str, v: Union[float, int]) -> tuple:
    """
    Type-annotated function that takes a string an an int or float and
    returns a tuple. The first element of the tuple is a string and
    the second is the square of the int/float annotated as a float.
    """
    return (k, float(v ** 2))
