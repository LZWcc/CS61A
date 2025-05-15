"""
>>> s = [3, 4, 5]
>>> t = iter(s)
>>> next(t)
3
>>> next(t)
4
>>> u = iter(s)
>>> next(u)
3
>>> next(t)
5
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

"""
>>> s = [[1, 2], 3, 4, 5]
>>> t = iter(s)
>>> next(t)
[1, 2]
>>> next(t)
3
>>> list(t)
[4, 5]
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

"""
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d['zero'] = 0
>>> k = iter(d.keys()) # or iter(d)

>>> next(k)
'one'

>>> v = iter(d.values())
>>> next(v)
1

>>> i = iter(d.items())
>>> next(i)
('one', 1)
"""

"""
>>> bcd = ['b', 'c', 'd']
>>> [x.upper() for x in bcd]
['B', 'C', 'D']
>>> map(lambda x: x.upper(), bcd)
<map object at 0x7f8c4c0d3a90>
>>> m = map(lambda x: x.upper(), bcd)
>>> next(m)
'B'
>>> next(m)
'C'
>>> next(m)
'D'
"""

def double(x):
    print('**', x, '=>', 2 * x, '**')
    return 2 * x
"""
>>> map(double, [3, 5, 7])
<map object at 0x7f8c4c0d3a90>
>>> m = map(double, [3, 5, 7])
>>> next(m)
** 3 => 6 **
6

>>> m = map(double, range(3, 7))
>>> f = lambda y: y >= 10
>>> t = filter(f, m)
>>> next(t)
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
10
>>> next(t)
** 6 => 12 **
12
>>> list(t)
[]
>>> list(filter(f, map(double, range(3, 7))))
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
** 6 => 12 **
[10, 12]
"""

"""
map	将函数应用到可迭代对象的每个元素上，返回结果的迭代器。
filter	筛选出满足条件的元素，返回结果的迭代器。
zip	将多个可迭代对象“打包”成元组的迭代器。
"""

"""
>>> t = [1, 2, 3, 2, 1]
>>> t
[1, 2, 3, 2, 1]
>>> reversed(t)
<list_reverseiterator object at 0x7f8c4c0d3a90>
>>> list(reversed(t))
[1, 2, 3, 2, 1]
>>> list(reversed(t)) == t
True
"""

"""
>>> list(zip([1, 2], [3, 4]))
[(1, 3), (2, 4)]
>>> list(zip([1, 2], [3, 4, 5]))
[(1, 3), (2, 4)]
>>> list(zip([1, 2], [3, 4, 5], [6, 7]))
[(1, 3, 6), (2, 4, 7)]
"""

def palidrome(s):
    """Return whether s is the same forwards and backwards."""
    return list(s) == list(reversed(s))
    return all([a == b for a, b in zip(s, reversed(s))])
"""
>>> s = [3, 1, 4, 1, 3]
>>> list(zip(s, reversed(s)))
[(3, 3), (1, 1), (4, 4), (1, 1), (3, 3)]
"""

