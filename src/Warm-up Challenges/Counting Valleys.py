#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/counting-valleys
An avid hiker keeps meticulous records of their hikes.
During the last hike that took exactly steps, for every step it was noted if it was an uphill U,
or a downhill D step.
Hikes always start and end at sea level, and each step up or down represents
a unit change in altitude. We define the following terms:

    A mountain is a sequence of consecutive steps above sea level,
    starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level,
    starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike,
find and print the number of valleys walked through. ."""

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    """
    Args:
        steps (int): len of the path.
        path (str): string with Ds/Us.

    Returns:
        int: number of valleys"""
    del steps
    current_height = 0
    valleys = 0
    # loop over steps and update current height
    for step in path:
        if step == 'D':
            current_height -= 1
        else:
            current_height += 1
            # update valley count if last step was U and we are back to height == 0
            if current_height == 0:
                valleys += 1
    return valleys


if __name__ == "__main__":
    ex_steps = 8
    ex_path = 'UDDDUDUU'

    result = countingValleys(ex_steps, ex_path)
    print(result)
