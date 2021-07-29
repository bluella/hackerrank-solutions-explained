#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/crush
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each the array element
between two given indices, inclusive. Once all operations have been performed,
return the maximum value in the array.
"""

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    """
    Args:
        n (int): len of zero arr.
        queries (list): 2d list with queries

    Returns:
        int: max element"""
    arr = [0] * (n + 1)
    # increase first el by query amount and decrease last of query amount
    for i in queries:
        arr[i[0] - 1] += i[2]
        arr[i[1]] -= i[2]

    # this way it's easy compute each el resulting value in one run
    ans = 0
    current = 0
    for i in arr:
        current += i
        if current > ans:
            ans = current
    return ans


if __name__ == "__main__":

    ex_arr = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    zero_arr_len = 10

    result = arrayManipulation(zero_arr_len, ex_arr)
    print(result)
