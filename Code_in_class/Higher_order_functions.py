"""
测试代码:
python3 -m doctest Higher_order_functions.py -v
"""
from operator import mul
from math import pi
def indentity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first n terms of a sequence.
    
    >>> summation(5, indentity)
    15
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first n natural numbers.
    
    >>> sum_naturals(5)
    15
    """
    return summation(n, indentity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    
    >>> sum_cubes(5)
    225
    """
    return summation(n, cube)

def pi_term(k):
    return 8 / mul(4 * k - 3, 4 * k - 1)
