#!/usr/bin/env python3
"""9-element_length.py"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function that returns a list of tuples, where each tuple
    contains an element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
