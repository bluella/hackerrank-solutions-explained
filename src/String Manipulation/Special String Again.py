#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/special-palindrome-again
A string is said to be a special string if either of two conditions is met:

    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria.
Given a string, determine how many special substrings can be formed from it.
"""

import math
import os
import random
import re
import sys
from collections import Counter


def substrCount(str_len, s):
    """
    Args:
        str_len (int): string len
        s (str): string

    Returns:
        int: how many special substrings are in s"""
    s_tuple = []  # string representation in a form of list of tuples
    count = 0  # counter of the cur
    cur_char = None  # tmp char
    special_substring_total_count = 0

    # represent string in a form of list of tuples
    # each tuple is (char, number of char occurences in a row)
    # and store it in the s_tuple
    for i in range(str_len):
        if s[i] == cur_char:
            count += 1
        else:
            if cur_char is not None:
                s_tuple.append((cur_char, count))
            cur_char = s[i]
            count = 1
    s_tuple.append((cur_char, count))

    # count special substrings, which consist from the same char
    for char_tuple in s_tuple:
        special_substring_total_count += (
            char_tuple[1] * (char_tuple[1] + 1)) // 2

    # count special substrings, which have one unique char in the middle
    for i in range(1, len(s_tuple) - 1):
        if s_tuple[i - 1][0] == s_tuple[i + 1][0] and s_tuple[i][1] == 1:
            special_substring_total_count += min(
                s_tuple[i - 1][1], s_tuple[i + 1][1])

    return special_substring_total_count


if __name__ == "__main__":

    ex_s1 = 'aabcc'
    ex_str_len = 5

    result = substrCount(ex_str_len, ex_s1)
    print(result)
