# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:58:54 2020

@author: Anon
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return f'{self.numer}/{self.denom}'
    def __repr__(self):
        return f'fraction({repr(self.numer)}, {repr(self.denom)})'
    def numerator(self):
        return self.numer
    def denominator(self):
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
    def gcd(self, a, b):
        """
        input:
            a, b: assumes any positive integer
        output:
            given the appropriate inputs function returns the Greatest Common Denominator of a and b respectively
        
        NOTE:   is used as a helper function for lowest()       
        """
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    def lowest(self):
        newNumer = int(self.numerator() / self.gcd(self.numerator(), self.denominator()))
        newDenom = int(self.denominator() / self.gcd(self.numerator(), self.denominator()))
        return fraction(newNumer, newDenom)


# test
oneThirds = fraction(1, 3)
threeFourths = fraction(15, 20)
total = oneThirds + threeFourths
sub = total - fraction(17,22)
print(total)
print(sub)
print(repr(sub))