# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:48:36 2020

@author: =GV=
"""

def findroot(x, epsilon = 0.000000000000001):
    """
    Parameters
    ----------
    x : int/float
        assumes any integer or float greater than 0
    epsilon: float, optional
        assumes any float greater than 0; is the maximum relative error, default is 0.000000000000001

    Returns
    -------
    guess: float
        given the appropriate input returns the square root of x
    NOTE:   the epsilon of the function may be set depending on the degree of accuracy and/or runtime required
    """
    assert x >= 0, 'Invalid input, function does not calculate imaginary numbers.'
    if x == 0 or x == 1:
        return x
    elif x > 1:
        high = x
        low = 1
    else:
        high = 1
        low = x
    guess = (high - low)/2 + low
    while abs(x - guess**2) >= epsilon:
        if guess**2 > x:
            high = guess
        else:
            low = guess
        guess = (high - low)/2 + low
    return guess


# test
# print(findroot(81))