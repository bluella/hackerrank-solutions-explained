#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/mark-and-toys
Mark and Jane are very happy after having their first child.
Their son loves toys, so Mark wants to buy some.
There are a number of different toys lying in front of him,
tagged with their prices.
Mark has only a certain amount to spend,
and he wants to maximize the number of toys he buys with this money.
Given a list of toy prices and an amount to spend,
determine the maximum number of gifts he can buy.
"""

import math
import os
import random
import re
import sys


def maximumToys(prices, budget):
    """
    Args:
        prices (list): list of integers
        budget (int): how much we can spend

    Returns:
        int: toy count"""

    # in order to maximize number of toys we pick the cheapest ones first
    prices = sorted(prices)
    i = 0
    toy_count = 0
    # spend budget starting from the cheapest toys
    while budget > 0 and i <= len(prices) - 1:
        if budget >= prices[i]:
            toy_count += 1
            budget -= prices[i]
        i += 1

    return toy_count


if __name__ == "__main__":

    ex_arr = [2, 4, 24, 16]
    ex_budget = 24

    result = maximumToys(ex_arr, ex_budget)
    print(result)
