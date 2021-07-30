#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-bubble-sort
Given an array of integers, sort the array in ascending order
using the Bubble Sort algorithm above.
Once sorted, print the following three lines:

Array is sorted in numSwaps
First Element: firstElement
Last Element: lastElement
"""

import math
import os
import random
import re
import sys


def countSwaps(arr):
    """
    Args:
        arr (list): list of integers

    Returns:
        None"""
    swap_counter = 0
    len_arr = len(arr)
    # just implement bubble sort and count swaps during the run
    for i in arr:
        for j in range(len_arr - 1):
            if arr[j] > arr[j + 1]:
                swap_counter += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f'Array is sorted in {swap_counter} swaps.')
    print(f'First Element: {arr[0]}')
    print(f'Last Element: {arr[-1]}')


if __name__ == "__main__":

    ex_arr = [2, 4, 24, 16]

    countSwaps(ex_arr)
