class Account:
    """
    >>> tom_account = Account('Tom')
    >>> jim_account = Account('Jim')
    >>> tom_account.instrest
    0.02
    >>> tom_account.balance = 10
    >>> getattr(tom_account, 'balance')
    10
    >>> hasattr(tom_account, 'balance')
    True
    >>> m = map(tom_account.deposit, range(10, 20))
    >>> tom_account.balance
    10
    >>> next(m)
    20
    """
    instrest = 0.02
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


