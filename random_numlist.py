# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:15:13 2021

@author: =GV=
"""

import random

def randomNum(n):
    yield random.randrange(0,n + 1)
    yield from randomNum(n)


def norepeat(rNum):
    randomNum = next(rNum)
    yield randomNum
    yield from norepeat(i for i in rNum if not i == randomNum)
    
def randomNumlist(n):
    """
    Parameters
    ----------
    n : int
        assumes any positive integer

    Returns
    -------
    numList : list
        given the appropriate input returns a list of unique integers from 0 to n (inclusive) in random order
    NOTE:   function uses a generator norepeat() as a helper function that generates a series of unique random numbers
            from a generator randomNum() which in turn is its helper function that generates random numbers within the
            range of 0 to n (inclusive)
    """
    assert n > 0, 'Invalid input! Value must be integer greater than 0'
    num = randomNum(n)
    unique = norepeat(num)
    return [next(unique) for i in range(n + 1)]


# # test
# test = 50
# print(randomNumlist(test))