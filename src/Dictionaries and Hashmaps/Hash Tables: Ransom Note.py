#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/ctci-ransom-note
Harold is a kidnapper who wrote a ransom note,
but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it
and use them to create an untraceable replica of his ransom note.
The words in his note are case-sensitive and he must
use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note,
print Yes if he can replicate his ransom note exactly
using whole words from the magazine; otherwise, print No.
"""

import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    """
    Args:
        magazine (list): list of words
        note (list): list of words

    Returns:
        None"""
    if not set(note).issubset(magazine):
        print('No')
        return

    # count all words in magazine and note
    magazine_dict = {word: magazine.count(word) for word in magazine}
    note_dict = {word: note.count(word) for word in note}
    res = 'Yes'
    for word in note_dict:
        if word not in magazine_dict:
            res = 'No'
            break
        # check if we have enough words in magazine to create note
        elif magazine_dict[word] >= note_dict[word]:
            continue
        else:
            res = 'No'
            break

    print(res)


if __name__ == "__main__":

    ex_magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
    ex_note = ['give', 'one', 'grand', 'today']

    checkMagazine(ex_magazine, ex_note)
