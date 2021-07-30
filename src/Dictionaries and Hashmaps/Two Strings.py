#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/two-strings
Given two strings, determine if they share a common substring.
A substring may be as small as one character.
"""

import math
import os
import random
import re
import sys


def twoStrings(s1, s2):
    """
    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        str: 'YES' or 'NO'"""
    set1 = set(s1)
    set2 = set(s2)
    # check the itersection of two sets
    if set1 & set2 != set():
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":

    ex_s1 = 'gdsgrgwr'
    ex_s2 = 'gd'

    result = twoStrings(ex_s1, ex_s2)
    print(result)
