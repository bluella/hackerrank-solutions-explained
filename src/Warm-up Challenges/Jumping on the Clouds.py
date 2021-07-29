#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
The player can jump on any cumulus cloud having a number that
is equal to the number of the current cloud plus 1 or 2.
The player must avoid the thunderheads. Determine the minimum number of jumps
it will take to jump from the starting postion to the last cloud.
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0
if they are safe or 1 if they must be avoided. """

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    """
    Args:
        c (int): array of ones and zeros.
    Returns:
        int: min number of jumps"""
    current_cloud = 0
    jumps = 0
    len_c = len(c)
    # count jumps whilst looping over the clouds
    while current_cloud < len_c - 1:
        if len_c > current_cloud + 2:
            # check if we are able to do long jump
            if c[current_cloud + 2] == 0:
                current_cloud += 2
            # else do short jump
            else:
                current_cloud += 1
        else:
            current_cloud += 1
        jumps += 1
        # print(current_cloud, jumps)
    return jumps


if __name__ == "__main__":
    jumps_arr = [0, 1, 0, 0, 0, 1, 0]

    result = jumpingOnClouds(jumps_arr)
    print(result)
