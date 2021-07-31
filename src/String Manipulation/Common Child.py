#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/common-child
A string is said to be a child of a another string if it can be formed
by deleting 0 or more characters from the other string.
Letters cannot be rearranged. Given two strings of equal length,
what's the longest string that can be constructed such that it is a child of both?
"""

import math
import os
import random
import re
import sys


def commonChild(s1, s2):
    """
    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: common child max len"""
    prev = [0] * (len(s2) + 1)
    curr = [0] * (len(s2) + 1)

    # loop each string
    # increase max common child count if common char is found
    for s1_char in s1:
        for j, s2_char in enumerate(s2, 1):
            curr[j] = prev[j - 1] + \
                1 if s1_char == s2_char else max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[-1]


if __name__ == "__main__":

    ex_s1 = 'abc'
    ex_s2 = 'sdgab'

    result = commonChild(ex_s1, ex_s2)
    print(result)
