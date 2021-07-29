#!/usr/bin/env python3
"""There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are."""

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(number_of_socks, sock_arr):
    '''
    Args:
        n (int): len of the sock_arr.
        sock_arr (list): array with ints.

    Returns:
        int: number of sock pairs'''
    del number_of_socks
    unpaired_socks_arr = []
    sock_pair_count = 0
    # loop over array
    for sock in sock_arr:
        # add new pair
        if sock in unpaired_socks_arr:
            unpaired_socks_arr.remove(sock)
            sock_pair_count +=1
        # add to unpaired socks
        else:
            unpaired_socks_arr.append(sock)
        # print(unpaired_socks_arr)
    return sock_pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    print(ar)

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
    