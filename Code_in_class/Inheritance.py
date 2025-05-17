class Account:
    """A bank account."""
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
class CheckingAccount(Account):
    """A bank account that charges for withdrawals.
    >>> a = Account('John')
    >>> b = CheckingAccount('Jack')
    >>> a
    <__main__.Account object at 0x7f8c4c0b3d90>
    >>> b
    <__main__.CheckingAccount object at 0x7f8c4c0b3d90>
    >>> a.balance
    0
    >>> b.balance
    0
    >>> a.deposit(100)
    100
    >>> b.deposit(100)
    100
    >>> a.withdraw(10)
    90
    >>> b.withdraw(10)
    89
    """
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
# Objects-Oriented Design
class Bank():
    """不会从Account继承, 因为Bank has accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10) # 银行记住这个账户并且返回它
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []

    def open_account(self,  holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1

class A:
    z = -1
    def f(self, x):
        return B(x - 1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)

class C(B):
    def f(self, x):
        return x 

a = A()
b = B(1)
b.n = 5

class Ratio:
    """
    >>> half = Ratio(1, 2)
    >>> print(half)
    1/2
    >>> half
    Ratio(1, 2)

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    
    >>> Ratio(1, 3).__add__(Ratio(1, 6))
    Ratio(1, 2)
    """
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        if isinstance(other, int):
            return Ratio(self.numer + other * self.denom, self.denom)
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
    
    # 计算最大公约数并约分
        import math
        gcd = math.gcd(new_numer, new_denom)
        new_numer //= gcd
        new_denom //= gcd
        return Ratio(new_numer, new_denom)
                
"""
__init__ 方法在对象被构造时自动调用.
__repr__ 方法在对象被打印时自动调用.
__add__ 用于将一个对象与另一个对象相加.
__bool__ 用于将一个对象转换为布尔值.
__float__ 用于将一个对象转换为浮点数.

>>> zero, one, two = 0 , 1, 2
>>> one + two
3
>>> bool(zero), bool(one)
(True, False)

>>> one.__add__(two)
3
>>> zero.__bool__(), one.__bool__()
(False, True)


"""

"""
isinstance(object, classinfo)
object: 要检查的对象
classinfo: 可以是一个类或类型元组
返回值: 如果 object 是 classinfo 的实例或子类的实例，则返回 True, 否则返回 False。
"""