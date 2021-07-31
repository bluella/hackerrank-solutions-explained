#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/alternating-characters
You are given a string containing characters A and B
only. Your task is to change it into a string such
that there are no matching adjacent characters.
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
"""

import math
import os
import random
import re
import sys

def alternatingCharacters(s1):
    """
    Args:
        s1 (str): first string

    Returns:
        int: how many elements need to be deleted"""
    del_count = 0
    # check every pair of elements in a loop
    for i in range(len(s1) - 1):
        if s1[i] == s1[i + 1]:
            del_count += 1
    return del_count


if __name__ == "__main__":

    ex_s1 = 'AABBABAAAB'

    result = alternatingCharacters(ex_s1)
    print(result)
