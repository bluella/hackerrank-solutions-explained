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
from collections import Counter


def makeAnagram(s1, s2):
    """
    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: how many elements need to be deleted"""
    # counter is going to create a dict with char: freq for each char from string
    # counter works as sets (with the hashing) so it's very fast
    counter_a = Counter(s1)
    counter_b = Counter(s2)
    # calculate number of elements to eliminate
    diff1 = counter_a - counter_b
    diff2 = counter_b - counter_a
    return sum(diff1.values()) + sum(diff2.values())


if __name__ == "__main__":

    ex_s1 = 'abc'
    ex_s2 = 'dsvcba'

    result = makeAnagram(ex_s1, ex_s2)
    print(result)
