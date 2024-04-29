#!/usr/bin/env python3
"""
Module for a function that takes a list of floats and returns their sum.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function which takes a list of floats
    and returns their sum as a float.
    """
    return sum(input_list)