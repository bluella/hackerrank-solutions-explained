#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/frequency-queries
You are given queries. Each query is of the form two integers described below:
-1 x : Insert x in your data structure.
-2 y : Delete one occurence of y from your data structure, if present.
-3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
"""

import math
import os
import random
import re
import sys
from collections import Counter


def freqQuery(queries):
    """
    Args:
        queries (list): 2d list of queries

    Returns:
        list: after all queries processed"""
    freq = Counter()

    cnt = Counter()

    arr = []

    # count numbers and change frequencies in a loop
    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1

        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1

        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)

    return arr


if __name__ == "__main__":

    ex_arr = [[1, 5], [1, 6], [3, 2], [1, 10], [3, 1]]

    result = freqQuery(ex_arr)
    print(result)
