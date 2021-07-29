#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/repeated-string
There is a string s of lowercase English letters that is repeated infinitely many times.
Given an integer n find and print the number of letter a's
in the first n letters of the infinite string.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    """
    Args:
        s (str): string to multiply.
        n (int): integer number of letter to take into account.
    Returns:
        int: number of a's"""
    i = 0
    len_s = len(s)
    a_counter = 0
    # count a's in whole repeated s's
    for i in range(len_s):
        if s[i] == "a":
            a_counter += 1
    a_counter = a_counter * (n // len_s)

    # count a's in remainder
    for i in range(n % len_s):
        if s[i] == "a":
            a_counter += 1
        # print(i, a_counter)

    return a_counter


if __name__ == "__main__":
    ex_str = "aba"
    ex_n = 10

    result = repeatedString(ex_str, ex_n)
    print(result)
