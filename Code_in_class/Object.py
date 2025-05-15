class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        """Deposit amount into the account."""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
"""
>>> a = Account('Alice')
>>> a.balance
0
>>> a.balance = 12
>>> a.balance
12

>>> b = Account('Bob')
>>> b.balance
0
>>> b.balance = 20
>>> a.backup = b
>>> a.backup.balance
20
"""