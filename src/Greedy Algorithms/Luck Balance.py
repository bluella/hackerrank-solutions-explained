#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/luck-balance
Lena is preparing for an important coding competition
that is preceded by a number of sequential preliminary contests.
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory.
Each contest is described by two integers, L[i] and T[i]:

L[i] is the amount of luck associated with a contest.
If Lena wins the contest, her luck balance will decrease by L[i];
if she loses it, her luck balance will increase by L[i].

T[i] denotes the contest's importance rating.
It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

If Lena loses no more than k
important contests, what is the maximum amount of luck
she can have after competing in all the preliminary contests?
This value may be negative.
"""

import math
import os
import random
import re
import sys
import heapq


def luckBalance(max_lost_contests, contests):
    """
    Args:
        max_lost_contests (int): how many contests could be lost
        contests (list): 2d array of integers

    Returns:
        int: max amount of luck"""
    most_luck = 0
    important_contests = []

    # if the contest is unimportant, then we loose it to increase luck balance
    for contest in contests:
        if contest[1] == 0:
            most_luck += contest[0]
        else:
            important_contests.append(contest[0])
    # if the contest is important we pick the largest ones to loose
    most_luck += sum(heapq.nlargest(max_lost_contests, important_contests))
    most_luck -= sum(heapq.nsmallest(len(important_contests) -
                     max_lost_contests, important_contests))
    return most_luck


if __name__ == "__main__":

    ex_max_lost_contests = 2
    ex_contests = [[3, 0], [2, 1], [5, 1]]

    result = luckBalance(ex_max_lost_contests, ex_contests)
    print(result)
