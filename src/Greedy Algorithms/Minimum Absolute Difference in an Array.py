#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
Given an array of integers,
find the minimum absolute difference between any two elements in the array.
"""

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    """
    Args:
        arr (list): list of integers

    Returns:
        int: min abs diff"""
    # min abs difference is gonna be between the next elements
    arr.sort()
    return min([abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1)])


if __name__ == "__main__":

    ex_arr = [1, 6, 2, 11]

    result = minimumAbsoluteDifference(ex_arr)
    print(result)
