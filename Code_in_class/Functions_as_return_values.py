def make_adder(n):
    """Return a function that takes one argument k and returns n + k.
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return n + k
    return adder