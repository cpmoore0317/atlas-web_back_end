#!/usr/bin/env python3
"""
Module for annotating the function with correct types.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function that returns a list of tuples, where each tuple
    contains an element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
