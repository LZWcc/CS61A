def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 ==0:
            print("fizzbuzz")
        elif k % 3 == 0:
            print("fizz")
        elif k % 5 == 0:
            print("buzz")
        else:
            print(k)
        k += 1
    return None
    "*** YOUR CODE HERE ***"

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n < 2:
        return False
    i = 2;
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    "*** YOUR CODE HERE ***"

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    unique = 0
    i = 0
    while i < 10:
        if has_digit(n, i):
            unique += 1
        i += 1
    return unique
    "*** YOUR CODE HERE ***"

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    while n:
        if n % 10 == k:
            return True
        n = n // 10
    return False
    "*** YOUR CODE HERE ***"

def repeating(t, n):
    """Return whether t digits repeat to form positive integer n.

    >>> repeating(1, 6161)
    False
    >>> repeating(2, 6161)  # repeats 61 (2 digits)
    True
    >>> repeating(3, 6161)
    False
    >>> repeating(4, 6161)  # repeats 6161 (4 digits)
    True
    >>> repeating(5, 6161)  # there are only 4 digits
    False
    """
    if pow(10, t-1) > n:  # make sure n has at least t digits
        return False
    end = n % pow(10, t)  # last t digits
    rest = n
    while rest:
        if rest % pow(10, t) != end:
           return False
        rest = rest // pow(10, t)
    return True