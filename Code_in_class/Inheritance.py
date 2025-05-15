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