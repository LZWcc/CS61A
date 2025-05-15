def make_adder(n):
    def adder(k):
        return n + k
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

compose1(square, make_adder(2))(3) # (3 + 2)^2 = 25

def curry2(f):
    """Return a curried version of f."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

same_curry2 = lambda f : lambda x : lambda y : f(x, y)

tmp = lambda x : x * x
tmp1 = lambda x : lambda y : x * y
