#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/count-triplets-1
You are given an array and you need to find number of tripets of indices: i,j,k
such that the elements at those indices are in geometric progression for a given common ratio r
and i < j < k
"""

import math
import os
import random
import re
import sys
from collections import defaultdict


def countTriplets(arr, r):
    """
    Args:
        arr (list): list of integers
        r (int): geometric progression multiplier

    Returns:
        int: substring anagrams count"""
    count = 0
    numbers_dict = {}
    pairs_dict = {}

    # count numbers in a loop
    # count corresponding pairs in a loop
    for i in reversed(arr):
        # increase count if we have a corresponding pair for the number
        if i * r in pairs_dict:
            count += pairs_dict[i * r]
        if i * r in numbers_dict:
            pairs_dict[i] = pairs_dict.get(i, 0) + numbers_dict[i * r]

        numbers_dict[i] = numbers_dict.get(i, 0) + 1

    return count


if __name__ == "__main__":

    ex_arr = [2, 4, 8, 16]
    ex_r = 2

    result = countTriplets(ex_arr, ex_r)
    print(result)
