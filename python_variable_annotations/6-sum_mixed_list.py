#!/usr/bin/env python3
"""
Module for returning the sum of a list with mied types.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Type-annotated function which takes a list of integers and floats
    and returns their sum as a float.
    """
    return sum(mxd_list)
