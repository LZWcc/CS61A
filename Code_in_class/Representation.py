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
>>> print(half)
1/2
'Fraction(1, 2)'
>>> str(half)
'1/2'
"""

