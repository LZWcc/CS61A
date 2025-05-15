"""
str对人类可读
repr对python解释器可读
>>> 12e12
12000000000000.0
>>> print(repr(12e12))
12000000000000.0
>>> eval(repr(object)) == object
True
>>> eval(repr(object)) is object
True

>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> print(half)
1/2
>>> str(half)
'1/2'
"""

"""
>>> s = "Hello, world!"
>>> s
'Hello, world!'
>>> print(repr(s))
'Hello, world!'
>>> print(s)
Hello, world!
>>> print(str(s))
Hello, world!
>>> str(s)
'Hello, world!'
>>> repr(s)
"'Hello, world!'"
"""

"""
>>> from math import pi
>>> f'pi start with {pi}...'
'pi start with 3.141592653589793...'
"""

# Polymorphic Functions 多态函数
"""
>>> half = Fraction(1, 2)
>>> half.__repr__ ()
'Fraction(1, 2)'
>>> half.__str__ ()
'1/2'

"""

def repr(x):
    return type(x).__repr__(x)
