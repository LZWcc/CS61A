# Tree-Structed Data
def tree(labal, branches=[]):
    return [labal] + list(branches)

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_leaf(t):
    return not branches(t)

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

"""实现bigs函数, 它接受包含整数标签的树实例, 它返回t中所有标签大于其祖先标签的节点数量"""
def bigs(t):
    """
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0), [Tree(2)]])])
    >>> bigs(a)
    4
    """
    # a 是当前遍历到的节点（Tree 实例）.
    # x 是当前节点所有祖先标签中的最大值.
    def f(a, x):
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else:
            return sum([f(b, x) for b in a.branches])
    return f(t, t.label - 1)

def bigss(t):
    n = [0]
    def f(a, x):
        if a.label > x:
            n[0] += 1
        for b in a.branches:
            f(b, a.label)
    f(t, t.label - 1)
    return n[0]