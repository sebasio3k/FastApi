
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance # encapsulation
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        else:
            return "Deposit amount must be positive."
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance is {self.__balance}."
        else:
            return "Insufficient funds. Withdrawal amount must be positive and less than or equal to the current balance."
    
    def check_balance(self):
        return f"Current balance is {self.__balance}."


account = BankAccount("Bastian", 1000)  # instantiation, Abstraction

print(account.check_balance())
print(account.deposit(500))
print(account.deposit(0))
print(account.deposit(-1))
print(account.withdraw(200))
print(account.withdraw(20000))
print(account.withdraw(-10))
print(account.check_balance())