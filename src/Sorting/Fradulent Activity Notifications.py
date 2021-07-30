#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/fraudulent-activity-notifications
HackerLand National Bank has a simple policy for warning
clients about possible fraudulent account activity.
If the amount spent by a client on a particular day is greater than or equal to

2 X the client's median spending for a trailing number of days,
they send the client a notification about potential fraud.
The bank doesn't send the client any notifications until
they have at least that trailing number of prior days' transaction data.

Given the number of trailing days
and a client's total daily expenditures for a period of days,
determine the number of times the client will receive a notification over all days.
"""

import math
import os
import random
import re
import sys


def activityNotifications(expenditure, days):
    """
    Args:
        expenditure (list): list of integers
        days (int): number of ints used for median calculation

    Returns:
        int: notice count"""

    freq = {}
    notification_count = 0

    def find(idx):
        '''find ith order element from freq dict'''
        total_count = 0
        # expenditure is limited by 200
        for i in range(201):
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i

    # go through each day spend
    for i in range(len(expenditure) - 1):
        # accumulate frequencies to calculate median fast
        if expenditure[i] in freq:
            freq[expenditure[i]] += 1
        else:
            freq[expenditure[i]] = 1

        # check conditions to send notifications
        if i >= days - 1:
            if days % 2 == 0:
                median = (find(days // 2) + find(days // 2 + 1)) / 2
            else:
                median = find(days / 2)

            if expenditure[i + 1] >= (median * 2):
                notification_count += 1
                print("notification_count: ", notification_count)
            # remove the previous element from dictionary
            freq[expenditure[i - days + 1]] -= 1

    return notification_count


if __name__ == "__main__":

    ex_arr = [10, 20, 30, 40, 50]
    ex_budget = 3

    result = activityNotifications(ex_arr, ex_budget)
    print(result)
