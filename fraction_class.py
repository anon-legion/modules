# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:58:54 2020

@author: =GV=
"""
# import sys
from GCD_euclids_recursion import gcdRecur as gcd

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return f'{self.numer}/{self.denom}'
    def __repr__(self):
        return f'fraction({repr(self.numer)}, {repr(self.denom)})'
    def numerator(self):    # getter
        return self.numer
    def denominator(self):  # getter
        return self.denom
    def __add__(self, other):
        newDenom = self.denominator() * other.denominator()
        newNumer = self.numerator() * other.denominator() + other.numerator() * self.denominator()
        return fraction(newNumer, newDenom).lowest()
    def __sub__(self, other):
        newDenom = self.denominator() * other.denominator()
        newNumer = self.numerator() * other.denominator() - other.numerator() * self.denominator()
        return fraction(newNumer, newDenom).lowest()
    def convert(self):
        return self.numerator() / self.denominator()    
    def lowest(self):
        newNumer = int(self.numerator() / gcd(self.numerator(), self.denominator()))
        newDenom = int(self.denominator() / gcd(self.numerator(), self.denominator()))
        return fraction(newNumer, newDenom)

# print(sys.path)
# test
# oneThirds = fraction(1, 3)
# threeFourths = fraction(15, 20)
# total = oneThirds + threeFourths
# sub = total - fraction(17,22)
# print(total)
# print(sub)
# print(repr(sub))
