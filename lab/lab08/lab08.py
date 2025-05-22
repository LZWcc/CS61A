def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t0 = Tree(9)
    >>> add_d_leaves(t0, 4)
    >>> t0
    Tree(9)
    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def helper(tree, depth):
        for b in tree.branches:
            helper(b, depth + 1)
        for _ in range(depth):
            tree.branches.append(Tree(v))
    helper(t, 0)
    "*** YOUR CODE HERE ***"


def has_path(t, target):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular target.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(target) > 0, 'no path for empty target.'
    if t.label != target[0]:
        return False
    
    if len(target) == 1:
        return True
    for b in t.branches:
        if has_path(b, target[1:]):
            return True
    return False
    "*** YOUR CODE HERE ***"


def level_mutation_link(t, funcs):
	"""Mutates t using the functions in the linked list funcs.

	>>> t = Tree(1, [Tree(2, [Tree(3)])])
	>>> funcs = Link(lambda x: x + 1, Link(lambda y: y * 5, Link(lambda z: z ** 2)))
	>>> level_mutation_link(t, funcs)
	>>> t    # At level 0, apply x + 1; at level 1, apply y * 5; at level 2 (leaf), apply z ** 2
	Tree(2, [Tree(10, [Tree(9)])])
	>>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
	>>> level_mutation_link(t2, funcs)
	>>> t2    # Level 0: 1+1=2; Level 1: 2*5=10 => 10**2 = 100, 3*5=15; Level 2 (leaf): 4**2=16
	Tree(2, [Tree(100), Tree(15, [Tree(16)])])
	>>> t3 = Tree(1, [Tree(2)])
	>>> level_mutation_link(t3, funcs)
	>>> t3    # Level 0: 1+1=2; Level 1: 2*5=10; no further levels, so apply remaining z ** 2: 10**2=100
	Tree(2, [Tree(100)])
	"""
	if funcs is Link.empty:
		return
	t.label = funcs.first(t.label)
	remaining = funcs.rest
	if t.is_leaf() and remaining is not Link.empty:
		while remaining is not Link.empty:
			t.label = remaining.first(t.label)
			remaining = remaining.rest
	for b in t.branches:
		level_mutation_link(b, remaining)


def merge_numbers(n1, n2):
    """Merges two numbers that have decreasing digits.

    >>> merge_numbers(31, 42)
    4321
    >>> merge_numbers(21, 0)
    21
    >>> merge_numbers(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    if n1 % 10 < n2 % 10:
        return n1 % 10 + merge_numbers(n1 // 10, n2) * 10
    else:
        return n2 % 10 + merge_numbers(n1, n2 // 10) * 10
    "*** YOUR CODE HERE ***"


def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list,
    but with item added to the front of each. You can assume that
    nested_list is a list of lists.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + x for x in nested_list]
    "*** YOUR CODE HERE ***"

def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    # rest_s被赋值为[[], [3], [2], [2, 3]]
    # 执行insert_into_all(1, rest_s)，生成[[1], [1, 3], [1, 2], [1, 2, 3]]
    if s == []:
        return [s]
    else:
        rest_s = subseqs(s[1:])
        return rest_s + insert_into_all(s[0], rest_s)
        # 不包含第一个元素的子序列 + 包含第一个元素的子序列


def non_decrease_subseqs(s):
    """Return a nested list of all subsequences of S (a list of lists) 
    for which the elements of the subsequence are nondecreasing. The 
    subsequences can appear in any order. You can assume S is a list.

    >>> seqs = non_decrease_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_decrease_subseqs([])
    [[]]
    >>> seqs2 = non_decrease_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0]) # 包含当前元素, 下一个元素的prev需要更新为当前元素
            b = subseq_helper(s[1:], prev) # 不包含当前元素, prev保持不变
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)


def perms(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> p = perms([100])
    >>> type(p)
    <class 'generator'>
    >>> next(p)
    [100]
    >>> try: # Prints "No more permutations!" if calling next would cause an error
    ...     next(p)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(perms((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(perms("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not seq:
        yield []
    else:
        for p in perms(seq[1:]):
            for i in range(len(seq)):
                yield p[:i] + [seq[0]] + p[i:]
    "*** YOUR CODE HERE ***"


def shuffle_pairs(lst):
    """Swap adjacent pairs of elements in place.

    >>> nums = list(range(6))
    >>> shuffle_pairs(nums)
    >>> nums
    [1, 0, 3, 2, 5, 4]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle_pairs(letters)
    >>> letters
    ['b', 'a', 'd', 'c', 'f', 'e', 'h', 'g']
    >>> multiples = [10, 20, 30, 40]
    >>> shuffle_pairs(multiples)
    >>> multiples
    [20, 10, 40, 30]
    >>> pair = [1, 2]
    >>> shuffle_pairs(pair)
    >>> pair
    [2, 1]
    >>> empty = []
    >>> shuffle_pairs(empty)
    >>> empty
    []
    """
    assert len(lst) % 2 == 0, 'len(lst) must be even'
    half = len(lst) // 2
    for i in range(half):
        lst[2*i], lst[2*i+1] = lst[2*i+1], lst[2*i]


def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {
    ...     "bob": "Team A",
    ...     "barnum": "Team B",
    ...     "beatrice": "Team C",
    ...     "bernice": "Team B",
    ...     "ben": "Team D",
    ...     "belle": "Team A",
    ...     "bill": "Team B",
    ...     "bernie": "Team B",
    ...     "baxter": "Team A"
    ... }
    >>> player_dict = common_players(full_roster)
    >>> type(player_dict) == dict
    True
    >>> for key, val in sorted(player_dict.items()):
    ...     print(key, list(sorted(val)))
    Team A ['baxter', 'belle', 'bob']
    Team B ['barnum', 'bernice', 'bernie', 'bill']
    Team C ['beatrice']
    Team D ['ben']
    """
    result_dict = {}
    for player in roster:
        team = roster[player]
        # 如果存在，将 player 添加到对应 team 的列表中
        if team in result_dict:
            result_dict[team].append(player)
        else:
            result_dict[team] = [player]
    return result_dict
    "*** YOUR CODE HERE ***"
    


# You do not need to understand what this function does. It is used for testing.
def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]
    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random

### Phase 1: The Player Class
class Player:
    """
    >>> random = make_test_random()
    >>> p1 = Player('Hill', random)
    >>> p2 = Player('Don', random)
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135
    >>> p1.speech(p2)
    >>> p1.votes
    13
    >>> p1.popularity
    148
    >>> p2.votes
    10
    >>> p2.popularity
    99
    >>> for _ in range(4):  # 0.1, 0.2, 0.3, 0.4
    ...     p1.debate(p2)
    >>> p2.debate(p1)
    >>> p2.popularity
    49
    >>> p2.debate(p1)
    >>> p2.popularity
    0
    """
    def __init__(self, name, random_func):
        self.name = name
        self.votes = 0
        self.popularity = 100
        self.random_func = random_func

    def debate(self, other):
        random = self.random_func()
        p1 = self.popularity
        p2 = other.popularity
        tmp = p1 / (p1 + p2)
        p = max(0.1, tmp)
        if random < p:
            self.popularity =  max(0, 50 + self.popularity)
        else:
            self.popularity = max(0, self.popularity - 50)
        "*** YOUR CODE HERE ***"

    def speech(self, other):
        gain = self.popularity // 10
        self.votes += gain
        self.popularity += gain
        other.popularity = max(0, other.popularity - other.popularity // 10)
        "*** YOUR CODE HERE ***"

    def choose(self, other):
        return self.speech


### Phase 2: The Game Class
class Game:
    """
    >>> random = make_test_random()
    >>> p1, p2 = Player('Hill',random), Player('Don', random)
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> winner is g.winner()
    True
    >>> g.turn
    10
    >>> p1.votes = p2.votes
    >>> print(g.winner())
    None
    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over():
            if self.turn % 2 == 0:
                curr, other = self.p1, self.p2
            else:
                curr, other = self.p2, self.p1
            # curr.choose(other)(other)
            action = curr.choose(other)
            action(other)
            self.turn += 1
        "*** YOUR CODE HERE ***"
        return self.winner()

    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    def winner(self):
        if self.p1.votes > self.p2.votes:
            return self.p1
        elif self.p1.votes < self.p2.votes:
            return self.p2
        else:
            return None
        "*** YOUR CODE HERE ***"


### Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = AggressivePlayer('Don', random), Player('Hill', random)
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> p1.popularity = p2.popularity
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity += 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        if self.popularity <= other.popularity:
            return self.debate
        else:
            return self.speech
        "*** YOUR CODE HERE ***"

class CautiousPlayer(Player):
    """
    >>> random = make_test_random()
    >>> p1, p2 = CautiousPlayer('Hill', random), AggressivePlayer('Don', random)
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> # Additional correctness tests
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech
        "*** YOUR CODE HERE ***"


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if s is Link.empty or s.rest is Link.empty:
        return
    else:
        s.rest = s.rest.rest
        every_other(s.rest)
    "*** YOUR CODE HERE ***"


def slice_link(link, start, end):
    """Slices a linked list from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print(new)
    <1 4 1>
    """
    # 不需要包含任何元素（切片长度为0），所以返回空链表
    if end == 0:
        return Link.empty
    # 当前元素应该被包含在结果中，因为起始索引是0
    # 创建一个新的 Link 节点，其 first 是当前链表的第一个元素
    # 递归调用 slice_link 处理链表的其余部分，保持 start 为0，但 end 减1
    elif start == 0:
        # 已经消耗了一个元素位置。当我们把当前元素 link.first 放入结果中后
        # 需要从剩余元素 link.rest 中再获取 end - 1 个元素，而不是 end 个。
        return Link(link.first, slice_link(link.rest, 0, end - 1))
    else:
        # 当 start > 0 时，我们需要跳过当前元素 link.first
        # 跳过这个元素后，我们需要更新接下来要跳过的元素数量
        """
        减少 end 的原因
        同时，我们也需要更新 end。由于我们已经消耗了一个位置 (跳过了当前元素), 所以在链表的剩余部分中, 结束位置也要相应减少。
        原来我们要从当前位置取到 end 位置的元素，现在跳过了当前位置，所以相对于剩余链表，结束位置变成了 end - 1。
        """
        return slice_link(link.rest, start-1, end-1)
    "*** YOUR CODE HERE ***"


class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines


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
