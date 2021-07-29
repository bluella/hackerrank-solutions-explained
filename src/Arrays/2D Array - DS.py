#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/2d-array
An hourglass is a subset of values with indices:
a b c
  d
e f g
There are 16 hourglasses in 6x6 arr.
An hourglass sum is the sum of an hourglass values.
Calculate the hourglass sum for every hourglass in arr,
then print the maximum hourglass sum.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    """
    Args:
        arr (list): 2d list of numbers.

    Returns:
        int: max hourglass sum"""
    hour_glasses = []
    # loop over every top left corner of the hourglasses
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            # sum all values based on top left corner
            hour_glasses.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                                            arr[i+1][j+1] +
                                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    return max(hour_glasses)


if __name__ == "__main__":

    ex_arr = [[2, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1],]

    result = hourglassSum(ex_arr)
    print(result)
