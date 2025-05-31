"""
>>> abs(3)
3
>>> abs('hello')
Traceback (most recent call last):
  File "Calculator.py", line 1, in <module>
>>> Traceback (most recent call last):

"""

def double(x):
    if isinstance(x, str):
        raise TypeError("double takes only numbers")
    return x * 2

try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

def invert(x):
    result = 1 / x
    print('Never printed if x is 0')
    return result

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

from operator import add, mul, truediv, sub
def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
    
def reduce(f, s, initial):
    """Combine elements of s using f starting with initial.
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce_recursive(f, s, initial):
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce_recursive(f, rest, f(initial, first))
    
def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval) 
        return calc_apply(exp.first, arguments) # exp.first is +, -, *, /
    else:
        raise TypeError
    
def calc_apply(op, args):
    if not isinstance(op, str):
        raise TypeError(str(op) + ' is not a string')
    if op == '+':
        return reduce(add, args, 0)
    elif op == '-':
        return reduce(sub, args, 0)
    elif op == '*':
        return reduce(mul, args, 1)
    elif op == '/':
        return reduce(truediv, args, 1)
    else:
        raise TypeError(f"Unknown operator {op}")