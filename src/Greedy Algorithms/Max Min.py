#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/angry-children
You will be given a list of integers and a single integer k.
You must create an array of length k from elements of such that its unfairness is minimized.
Unfairness of an array is calculated as max(A') - min(A')
"""

import math
import os
import random
import re
import sys
import heapq

def maxMin(subarr_len, arr):
    """
    Args:
        subarr_len (int): length of the subarray
        arr (list): list of ints

    Returns:
        int: min(max - min)"""
    # check all subarrs in the sorted arr
    arr = sorted(arr, reverse=True)
    return min(arr[i] - arr[i + subarr_len - 1]
               for i in range(len(arr) - subarr_len + 1))

if __name__ == "__main__":

    ex_max_lost_contests = 3
    ex_contests = [1, 4, 2, 5, 3, 9, 2]

    result = maxMin(ex_max_lost_contests, ex_contests)
    print(result)
