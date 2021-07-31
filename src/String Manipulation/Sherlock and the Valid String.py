#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string
Sherlock considers a string to be valid if all characters of the string
appear the same number of times.
It is also valid if he can remove just 1 character 1 at index in the string,
and the remaining characters will occur the same number of times.
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s1):
    """
    Args:
        s1 (str): first string

    Returns:
        str: 'YES' or 'NO'"""
    freq_diff = 0

    # Counter is the fastest way to count
    count_dict = Counter(s1)  # dict with count of each character
    # dict with count: freq of that count
    freq_count = Counter(count_dict.values())
    # we should have no more than two frequencies
    if len(freq_count) > 2:
        return 'NO'
    elif len(freq_count) == 1:
        return 'YES'
    else:
        okay = False
        for item, count in freq_count.items():
            if count == 1:
                okay = True
            # case when we have exactly one original element to delete
            if item == 1 and count == 1:
                break
            # case when we have e.g. 4 A's and 5 B's, and that's fine
            if freq_diff == 0:
                freq_diff += item
            else:
                freq_diff -= item
                if abs(freq_diff) != 1:
                    return 'NO'
        if not okay:
            return 'NO'
        else:
            return 'YES'


if __name__ == "__main__":

    ex_s1 = 'abcabcc'

    result = isValid(ex_s1)
    print(result)
