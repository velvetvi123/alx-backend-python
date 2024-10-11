#!/usr/bin/env python3
"""Module for zoom_array function."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a new list with each element of the input tuple repeated.

    Args:
        lst: A tuple of elements
        factor: The number of times to repeat each element

    Returns:
        A list with each element from the input repeated 'factor' times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
