#!/usr/bin/env python3
"""7-to_kv.py"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function that takes a string an an int or float and
    returns a tuple. The first element of the tuple is a string and
    the second is the square of the int/float annotated as a float.
    """
    return (k, v ** 2)
