from operator import floordiv, mod

def divide_exact(n ,d):
    """Returns the quotient and remainder of n divided by d.
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)
q, r = divide_exact(2013, 10)
#print('整数部分', q)
#print('余数', r)