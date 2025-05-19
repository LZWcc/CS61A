class Link:
    """A linked list.
    >>> Link(3, Link(4, Link(5)))
    Link(3, Link(4, Link(5)))
    >>> s = Link(3, Link(4, Link(5)))
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.rest.first
    5
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> Link(8, s.rest)
    Link(8, Link(7, Link(5)))
    >>> s
    Link(3, Link(7, Link(5)))
    """
    empty = ()
    def __init__(self, first ,rest = empty):
        assert rest is Link.empty or isinstance(rest, Link) # 返回rest是否为Link
        self.first = first
        self.rest = rest
        
# Link(3, Link(4, Link(5), Link.empty))

# Linked List Processing
square, odd = lambda x: x * x, lambda x: x % 2 == 1
list(map(square, filter(odd, range(1, 6)))) # [1, 9, 25]

def range_link(start, end):
    """
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))
    
def map_link(f, s):
    """
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return Link.empty
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return Link.empty
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest
    
def add(s, v):
    """Add v to s, return modified s.
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(3, Link(5)))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(3, Link(4, Link(5))))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(3, Link(4, Link(5, Link(6)))))))
    """
    assert s is not Link.empty
    if s.first > v: # 插入值比当前节点值小, 在s的头部插入v
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty: # 插入值比当前节点值大，且当前不是最后一个节点
        s.rest = Link(v)
    elif s.first < v:   # 插入值比当前节点值大，且当前不是最后一个节点
        add(s.rest, v)
    return s
        
# Tree Class
class Tree:
    """A tree.
    >>> Tree(1)
    Tree(1)
    >>> Tree(1, [Tree(3), Tree(4)])
    Tree(1, [Tree(3), Tree(4)])
    >>> t = Tree(1, [Tree(3), Tree(4)])
    >>> print(t)
    1
        3
        4
    
    """
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branches_str)
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines
    
    def is_leaf(self):
        return not self.branches
    
def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves

def height(t):
    if t.is_leaf():
        return 0
    else:
        return 1 + max(height(b) for b in t.branches)

def prune(t, n):
    t.branches = [b for b in t.branches if height(b) >= n]
    for b in t.branches:
        prune(b, n)





def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
    
# Tree Abstract Data Type
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches) # list()将branches转换为列表

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    if len(tree) == 1:
        return True
    for branch in tree[1:]:
        if not is_tree(branch):
            return False
    return True

def label(tree):
    assert is_tree(tree)
    return tree[0] # 返回树的根节点

def branches(tree):
    assert is_tree(tree)
    return tree[1:] # 返回树的所有分支

def Fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = Fib_tree(n - 2)
        right = Fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])