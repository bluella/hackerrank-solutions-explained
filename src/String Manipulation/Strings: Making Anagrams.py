#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-making-anagrams
A student is taking a cryptography class and has found anagrams to be very useful.
Two strings are anagrams of each other if the first string's letters
can be rearranged to form the second string.
In other words, both strings must contain the same exact letters in the same exact frequency.
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings.
The encryption is dependent on the minimum number of character
deletions required to make the two strings anagrams. Determine this number.

Given two strings, that may or may not be of the same length,
determine the minimum number of character deletions required to make and anagrams.
Any characters can be deleted from either of the strings.
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
