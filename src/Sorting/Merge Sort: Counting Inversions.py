#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-merge-sort
Given an array return the number of inversions to sort the array.
"""

import math
import os
import random
import re
import sys


def merge_sort(arr):
    '''regular merge sort algo'''
    length = len(arr)
    mid = length // 2
    if length >= 2:
        sorted_0, counts_0 = merge_sort(arr[:mid])
        sorted_1, counts_1 = merge_sort(arr[mid:])
        result, counts = merge(sorted_0, sorted_1)
        return result, counts + counts_0 + counts_1
    else:
        return arr, 0


def merge(arr0, arr1):
    '''merge two sorted arrs'''
    inversions = 0
    result = []
    # two indices to keep track of where we are in the array
    i0 = 0
    i1 = 0
    # probably doesn't really save much time but neater than calling len()
    # everywhere
    len0 = len(arr0)
    len1 = len(arr1)
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            # count the inversion right here: add the length of left array
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions


def countInversions(arr):
    '''wrapper around merge sort'''
    sorted_arr, inversions = merge_sort(arr)
    del sorted_arr
    # print(final_array)
    return inversions


if __name__ == "__main__":

    ex_arr = [2, 4, 24, 16]

    res = countInversions(ex_arr)
    print(res)
