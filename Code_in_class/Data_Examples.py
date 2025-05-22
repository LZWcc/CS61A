"""
>>> t = [1, 2, 3]
>>> t[1:3] = [t]
>>> t.extend(t)

>>> t = [[1, 2], [3, 4]]
>>> t[0].append(t[1:2])
"""
# 当通过实例的名称查找属性时，Python会在找到类的属性之前先查找实例的属性。
# 如果在实例中找到了属性，则返回该属性；否则，Python会在类中查找该属性。

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    
    def work(self):
        return self.greeting + ', I work'
    
    def __repr__(self):
        # repper方法在运行交互式会话时显示工人实例的字符串
        return Bourgeoisie.greeting

# 资产阶级
class Bourgeoisie(Worker):
    """
    >>> Worker().work()
    'Sir, I work'

    >>> jack = Worker()
    >>> john = Bourgeoisie()
    >>> jack.greeting = 'Maam'
    >>> jack
    Peom
    >>> jack.work()
    'Maam, I work'

    >>> john.work()
    Peom, I work
    'I gather wealth'

    >>> john.elf.work(john)
    'Peom, I work'
    """
    greeting = 'Peom'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'
    
def min_abs_indices(s):
    """
    >>> min_abs_indices([1, 2, 3])
    [0]
    >>> min_abs_indices([1, 2, 3, 4])
    [0]
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> min(s)
    -4
    >>> min(s, key = abs)
    -2
    >>> min(map(abs, s))
    2
    """
    min_abs = min(map(abs, s)) # 在新的可迭代对象上寻找最小值
    f = lambda x: abs(s[x]) == min_abs # 过滤器函数
    s = list(filter(f, range(len(s))))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs] # 返回最小值的索引
    
def largest_adj_sum(s):
    """
    >>> largest_adj_sum([1, 2, 3])
    5
    >>> largest_adj_sum([1, 2, 3, 4])
    7
    >>> largest_adj_sum([1, 2, -3, -4])
    2
    >>> largest_adj_sum([1, -2, -3, -4])
    -5
    """
    list(zip(s[:-1], s[1:])) # 创建所有相邻元素对
    #  除了最后一个元素以外的所有元素, 从第二个元素开始的所有元素
    return max(s[i] + s[i + 1] for i in range(len(s) - 1)) # 返回最大值
    
def digit_dict(s):
    """字典的值包含以该数字结尾的所有数字的列表
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 5: [5, 55], 8: [8], 9: [89]}
    >>> {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}
    """
    last_digits = [x % 10 for x in s] # 取出最后一位数字
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits} # 生成字典

def all_have_an_equal(s):
    """Does every element equal some other element in s?
    >>> all_have_an_equal([1, 2, 3])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    >>> s = [4, 3, 2, 3, 2, 4]
    >>> i = 1
    >>> s[:i]
    [4]
    >>> s[i+1:]
    [2, 3, 2, 4]
    >>> s[:i] + s[i+1:]
    [4, 2, 3, 2, 4]
    >>> s[i] in s[:i] + s[i+1:]
    True
    >>> all(s[i] in s[:i] + s[i+1:] for i in range(len(s)))
    True
    >>> min([s.count(x) for x in s]) > 1
    True
    """
    return min([s.count(x) for x in s]) > 1


def ordered(s, key = lambda x: x):
    """Is Link s ordered? 使用递归解决, 检查前两个元素有序, 并确保之后的元素也有序
    >>> ordered(Link(1, Link(3, Link(5))))
    True
    >>> ordered(Link(1, Link(3, Link(2))))
    False
    >>> ordered(Link(1, Link(-3, Link(5))), key = abs)
    True
    """  
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) > key(s.rest.first):
        return False
    else:
        return ordered(s.rest, key) # 递归调用, 检查下一个元素是否有序
    
def merge(s, t):
    """Return a sorted Link with the elements of s & t
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        # 创建一个以最小元素s.first为首的链表, 其后是s中的其他所有元素和t中的所有元素的合并版本
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))
    
def merge_in_place(s, t):
    """Return a sorted Link with the elements of s & t
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t) 
        return s
    else:
        t.rest = merge_in_place(s, t.rest) 
        return t
    
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'