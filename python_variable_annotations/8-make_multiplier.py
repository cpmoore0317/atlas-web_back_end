#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that takes a multiplier float and returns a
    function that multiplies that multiplier by another float.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
