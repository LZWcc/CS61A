def path(m, n):
    if m < 1 or n < 1:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return path(m - 1, n) + path(m, n - 1)
    
def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if not s: # if s == []
        return 1
    
    # 辅助函数，表示从索引i开始的子数组的最大乘积
    def helper(i):
        if i >= len(s):
            return 1
        choose = s[i] * helper(i + 2)
        skip = helper(i + 1)
        return max(choose, skip)
    return helper(0)

    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))
        # or
        return max(s[0] * max_product(s[2:]), s[1] * max_product(s[3:]))
    "*** YOUR CODE HERE ***"

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [[k] + rest for rest in sums(n - k, m) if rest == [] or k != rest[0]]
    return result

res = sums(5, 5)