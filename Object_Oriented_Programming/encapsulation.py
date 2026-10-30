class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance           # hidden from outside

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

acct = BankAccount("Sam", 100)
acct.deposit(50)
print(acct.balance)        # 150
# acct.__balance           # AttributeError