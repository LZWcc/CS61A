def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    """
    >>> fib = count(fib)
    >>> fib(5)
    5
    >>> fib.calls
    15
    >>> fib(5)
    5
    >>> fib.calls
    30
    """
    def counted(n):
        counted.calls += 1
        return f(n)
    counted.calls = 0
    return counted

# Memoization
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# Exponentiation
def fast_pow(a, b):
    ans = 1
    while b:
        if b % 2 == 1:
            ans *= a
        a *= a
        b //= 2
    return ans

def fast_pow_recursive(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_pow_recursive(b, n // 2))
    else:
        return b * fast_pow_recursive(b, n - 1)
def square(x):
    return x * x

"""-------------------------------"""
# 计算递归函数执行过程中的最大栈帧数（递归深度）
def count_frames(f):
    """
    >>> fib = count_frames(fib)
    >>> fib(20)
    5
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    """
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
    