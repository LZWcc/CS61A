"""
draw 函数接收两个参数：
hand: 一个列表
positions: 由唯一非负整数构成的列表, 且所有整数均小于 hand 的长度

函数的功能是：
根据 positions 中的每个索引 p, 移除 hand[p] 对应的元素
返回被移除的元素列表，元素的顺序需与其在 hand 中的原始顺序一致（而非 positions 中的顺序）

填空选项：
从以下名称中选择填入每个空白处：
list, map, filter, reverse, reversed, sort, sorted, append, insert, index, remove, pop, zip, sum
（具体用法请参考 Python 内置函数和列表方法的文档说明）

讨论环节：
在编写代码前，请小组讨论以下问题以确保正确实现功能：
如何确保移除正确的元素并按原始顺序返回？
避免盲目试错！讨论的目的是通过逻辑分析解决问题，而非依赖解释器验证。
"""

"""
Hint:
对于列表 s 和整数 i, s.pop(i) 会返回并删除第 i 个元素。此操作会导致：

后续元素的索引位置发生改变（向前移动一位）

前面的元素的索引位置不受影响

调用 reversed(s) 会返回一个反向迭代器。若需得到反转后的列表, 需显式转换为列表: list(reversed(s))。
"""
def draw(hand, positions):
    """Remove and return the items at positions from hand.

    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))

"""
Q2: 键盘
概述：键盘上每个字母对应一个按钮。按下按钮时，它会通过调用输出函数（如 print)输出字母。字母的大小写取决于 Caps Lock 键被按下的次数。

第一步：实现 Button 类

Button 类接收一个小写字母（字符串）和一个单参数输出函数，例如 Button('c', print)。

Button 的 press 方法会调用其 output 属性（一个函数），并根据 caps_lock 的按下次数决定输出字母的大小写：

如果 caps_lock 被按下奇数次，输出大写字母。

否则，输出小写字母。

press 方法还会递增 pressed 并返回被按下的键。
提示：'hi'.upper() 的结果是 'HI'。

第二步：实现 Keyboard 类

Keyboard 类有一个字典 keys, 其中包含 LOWERCASE_LETTERS 中每个字母对应的 Button(以字母作为键)。

它还有一个 typed 列表，存储已键入的字母（可能混合大小写）。

type 方法接收一个仅包含小写字母的字符串 word, 并依次调用 keys 中对应字母的 Button 的 press 方法，将字母（根据 caps_lock 决定大小写）添加到 Keyboard 的 typed 列表中。
重要：在 type 方法的实现中，不要直接使用 upper 或 letter,而是调用 press。

阅读 doctests 并讨论以下问题：

为什么可以通过 .press().press().press() 连续多次按下按钮？

为什么连续按下按钮时，有时只打印一行，有时打印多行？

为什么 bored.typed 最后会有 10 个元素？

讨论时间：
在编写代码之前，请讨论以下问题：

Button 类:letter 和 output 属性将如何被使用？

Keyboard 类:typed 和 keys 将如何被使用？每次按下 keys 中的按钮时，如何将新字母添加到 typed 列表中？
如果不确定，可以咨询助教！当所有人都理解这些问题后，再尝试一起编写代码。
"""

LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1

class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was pressed."""
        self.pressed += 1
        if self.caps_lock.pressed % 2 == 0:
            self.output(self.letter)
        else:
            self.output(self.letter.upper())
        return self
        "*** YOUR CODE HERE ***"


class Keyboard:
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """
    def __init__(self):
        self.typed = []
        self.keys = {letter : Button(letter, self.typed.append) for letter in LOWERCASE_LETTERS}  # Try a dictionary comprehension!

    def type(self, word):
        """Press the button for each letter in word."""
        assert all([w in LOWERCASE_LETTERS for w in word]), 'word must be all lowercase'
        for w in word:
            self.keys[w].press()
        "*** YOUR CODE HERE ***"

class Eye:
    """An eye.

    >>> Eye().draw()
    '0'
    >>> print(Eye(False).draw(), Eye(True).draw())
    0 -
    """
    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return '-'
        else:
            return '0'

class Bear:
    """A bear.

    >>> Bear().print()
    ? 0o0?
    """
    def __init__(self):
        self.nose_and_mouth = 'o'

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print('? ' + left.draw() + self.nose_and_mouth + right.draw() + '?')

class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ? -o-?
    """
    def next_eye(self):
        return Eye(True)
    "*** YOUR CODE HERE ***"

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ? -o0?
    """
    def __init__(self):
        super().__init__()
        self.eye_call = 0
        "*** YOUR CODE HERE ***"

    def next_eye(self):
        self.eye_call += 1
        return Eye(self.eye_call % 2)
        "*** YOUR CODE HERE ***"
