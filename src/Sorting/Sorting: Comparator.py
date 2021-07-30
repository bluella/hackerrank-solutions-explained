#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-comparator-sorting
Comparators are used to compare two objects. In this challenge,
you'll create a comparator and use it to sort an array.
The Player class is provided in the editor below.
"""

import math
import os
import random
import re
import sys
from functools import cmp_to_key


class Player:
    '''just name/score holder'''
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'{self.score} {self.name}'

    @staticmethod
    def comparator(a, b):
        '''Compare two players'''
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        elif a.name > b.name:
            return 1
        return -1


if __name__ == "__main__":

    data = [Player('Max', 2), Player('Kris', 1), Player('Kevin', 3)]
    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
