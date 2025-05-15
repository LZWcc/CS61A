def tree(label, branches=[]):
    '''其根标签可以是任何值, label(t) 返回该值'''
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1: # 任何分支必须是一个列表, 标签至少有一个元素
        return False
    for branch in branches(tree): # 所有的分支必须是树
        if not is_tree(branch):
            return False
    return True 

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right),[left, right])
    
def count_leaves(t):
    """递归统计树的叶子"""
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)
    
def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),  bs)

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    
def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)
    
def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == [label(t)]:  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        return any(has_path(b, p[1:]) for b in branches(t))
        
        for b in branches(t):
            if has_path(b, p[1:]):
                return True
        return False
        "*** YOUR CODE HERE ***"

def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if x == label(t):
        return [label[t]]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return[label(t)] + path
    return None