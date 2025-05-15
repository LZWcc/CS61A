from datetime import date, datetime
today = date(2015, 2, 20)
print(today.strftime("%B %d, %Y"))
from unicodedata import name, lookup
lookup('BABY').encode()
lookup('BABY')

suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] ['heart', 'diamond']

numerals = {'I': 1, 'V': 5, 'X': 10}
"""
>>> numerals
{'I': 1, 'V': 5, 'X': 10}
>>> numerals['X']
10
>>> numerals['X'] = 11
>>> numerals
{'I': 1, 'V': 5, 'X': 11}
>>> numerals['L'] = 50
>>> numerals
{'I': 1, 'V': 5, 'X': 11, 'L': 50}
>>> numerals.pop('X')
11
>>> numerals
{'I': 1, 'V': 5, 'L': 50}
"""

# Tuple
"""
>>> (3, 4, 5, 6)
(3, 4, 5, 6)
>>> 3, 4, 5, 6
(3, 4, 5, 6)
>>> ()
()
>>> tuple([3, 4, 5])
(3, 4, 5)
>>> (3, 4, 5) + (6, 7)
(3, 4, 5, 6, 7)
>>> 5 in (3, 4, 5)
True
# 元组是不可变的值, 这意味着可以把它们用作字典中的键 但是不能使用包含列表的元组
>>> {(1, 2): 3}
{(1, 2): 3}
>>> {[1, 2]: 3}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> s = ([1, 2], 3)
>>> s[0] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> s[0][0] = 4
>>> s
([4, 2], 3)
"""


def f(s = []):
    s.append(1)
    return len(s)
"""
>>> f()
1
>>> f()
2
>>> f()
3
"""

