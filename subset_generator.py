# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:17:46 2020

@author: =GV=
"""
"""
Parameters
----------
L : list
    assumes any list

Returns
-------
    subsets: list
        given the appropriate input returns all possible subsets of L
    NOTE:   both functions perform with similar time complexity O(2^n)
            genSubsets_recur() is a rescursive implementation while genSubset_iter()
            is an iterative implementation
"""
def genSubsets_recur(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets_recur(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

def genSubsets_iter(L):
    subsets = [[]]
    while len(L) > 0:
        temp = L.pop()
        new = []
        for element in subsets:
            new.append(element + [temp])
        subsets += new
    return subsets


# # test
# x = ['a','b','c']
# print('genSubsets_recur:')
# print(genSubsets_recur(x), '\n')
# print('genSubsets_iter:')
# print(genSubsets_iter(x))