#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams
Two strings are anagrams of each other if the letters of one
string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings
of the string that are anagrams of each other.
"""

import math
import os
import random
import re
import sys
from collections import defaultdict


def sherlockAndAnagrams(s):
    """
    Args:
        s (str): string

    Returns:
        int: substring anagrams count"""
    substrings = defaultdict(int)

    # count all substrings
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            # sort each substring to account for anagrams
            substrings[''.join(sorted(s[j:j + i]))] += 1

    ans = 0
    # if we have 3 same substrings it gives us 3 different pairs of anagrams
    for value in substrings.values():
        ans += value * (value - 1) // 2

    return ans


if __name__ == "__main__":

    ex_s1 = 'gdsgrgwr'

    result = sherlockAndAnagrams(ex_s1)
    print(result)
