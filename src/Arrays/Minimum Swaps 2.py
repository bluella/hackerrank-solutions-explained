#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/minimum-swaps-2
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n]
without any duplicates. You are allowed to swap any two elements.
Find the minimum number of swaps required to sort the array in ascending order.
"""

import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    """
    Args:
        arr (list): list of numbers.

    Returns:
        int: min number of swaps"""
    i = 0
    count = 0
    # since we know exact place in arr for each element
    # we could just check each one and swap it to right position if thats
    # required
    while i < len(arr):
        if arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            count += 1
        else:
            i += 1

    return count


if __name__ == "__main__":

    ex_arr = [1, 2, 3, 5, 4]

    result = minimumSwaps(ex_arr)
    print(result)
