#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation
A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
For example, if 2 left rotations are performed on array [1, 2, 3] then the array would become
[3, 2, 1]
Given an array
of integers and a number n perform n left rotations on the array.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#


def rotate_once(arr):
    '''First to Last'''
    arr.append(arr[0])
    del arr[0]


def rotLeft(arr, n_rotations):
    """
    Args:
        arr (list): list of numbers.
        n_rotations (int): rotate arr n times
    Returns:
        list: changed arr"""
    for i in range(n_rotations):
        rotate_once(arr)
    return arr


if __name__ == "__main__":

    ex_arr = [1, 2, 3]
    rotations = 1

    result = rotLeft(ex_arr, rotations)
    print(result)
