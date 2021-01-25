# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:42:41 2020

@author: =GV=
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    NOTE:   function uses Euclid's algorithm'
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


