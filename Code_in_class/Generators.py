def plus_minus(x):
    yield x
    yield -x
"""
>>> t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3
>>> t
<generator object plus_minus ...>
generator 是一种产生值而不是返回值的函数
"""
def evens(start, end):
    even = start + (start % 2)
    while even <= end:
        yield even
        even += 2
"""
>>> t = evens(2, 10)
>>> next(t)
2
>>> next(t)
4
"""

def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a, b):
    yield from a
    yield from b

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
        """
        for x in countdown(k - 1):
            yield x
        """

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
"""
>>> list(prefixes('both'))
['b', 'bo', 'bot', 'both']
"""

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
"""
>>> list(substrings('tops'))
['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
"""

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1) # with_m + without_m
    
def count_partitions(n, m):
    """ List partitions.
    >>> for p in count_partitions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in count_partitions(n - m, m)]
        without_m = count_partitions(n, m - 1)
        return exact_match + with_m + without_m
    
def partition(n, m):
    """Yield partitions
    >>> for p in partition(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    >>> s = list(partition(60, 50))
    >>> len(s)
    966370
    >>> next(partition(60, 50))
    '10 + 50'
    >>> t = partition(60, 50)
    >>> for _ in range(10):
    ...     print(next(t))
    10 + 50
    1 + 9 + 50
    2 + 8 + 50
    1 + 1 + 8 + 50
    3 + 7 + 50
    1 + 2 + 7 + 50
    1 + 1 + 1 + 7 + 50
    4 + 6 + 50
    1 + 3 + 6 + 50
    2 + 2 + 6 + 50
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partition(n - m, m):
            yield p + ' + ' + str(m)
        yield from partition(n, m - 1)