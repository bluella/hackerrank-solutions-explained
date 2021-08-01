#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/greedy-florist
A group of friends want to buy a bouquet of flowers.
The florist wants to maximize his number of new customers and the money he makes.
To do this, he decides he'll multiply the price of each flower by the number of that
customer's previously purchased flowers plus 1. The first flower will be original price:
(0 + 1) x price, the next will be
(1 + 1) x price
and so on.

Given the size of the group of friends,
the number of flowers they want to purchase and the original prices of the flowers,
determine the minimum cost to purchase all of the flowers.
The number of flowers they want equals the length of the
array.
"""

import math
import os
import random
import re
import sys
import heapq


def getMinimumCost(number_of_friends, flower_costs):
    """
    Args:
        number_of_friends (int): how many friends do we have
        flower_costs (list): list of ints

    Returns:
        int: min cost for all flowers"""
    friends_heap = [0] * number_of_friends
    heapq.heapify(friends_heap)
    total_cost = 0
    # the idea is to purchase the most expensive flowers
    # as the first flower for each of friends
    # this way we minimize total cost
    for cost in sorted(flower_costs, reverse=True):
        # heap is very efficient for consecutive get_min operations
        smallest_friend = heapq.heappop(friends_heap)
        total_cost += (1 + smallest_friend) * cost

        heapq.heappush(friends_heap, smallest_friend + 1)

    return total_cost


if __name__ == "__main__":

    ex_friends = 2
    ex_flowers = [1, 2, 3]

    result = getMinimumCost(ex_friends, ex_flowers)
    print(result)
