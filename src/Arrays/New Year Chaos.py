#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/new-year-chaos
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions,
but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(arr):
    """
    Args:
        arr (list): list of numbers.

    Returns:
        int: bribe count"""
    count = 0
    # loop over bribes
    for i in range(2):
        # loop over people in line
        for j in range(len(arr) - 1, 0, -1):
            # reverse the bribe
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                count += 1

    if arr == sorted(arr):
        print(count)
    else:
        print('Too chaotic')


if __name__ == "__main__":

    ex_arr = [2, 1, 3, 5, 6]

    minimumBribes(ex_arr)
