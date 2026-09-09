from abc import ABC, abstractmethod

class BankAccount(ABC): # Inheritance
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # encapsulation

    def _get_balance(self): # getter
        return self.__balance
    
    def _set_balance(self, new_balance): # setter
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError("Balance cannot be negative.")
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."
        else:
            return "Deposit amount must be positive."
    @abstractmethod
    def withdraw(self, amount): # Polymorphism
        pass # This method will be implemented in subclasses

    def check_balance(self):
        return f"Current balance is {self.__balance}."


class SavingsAccount(BankAccount): # Inheritance
    def withdraw(self, amount): # Polymorphism
        penalty = 0.05 * amount
        total = amount + penalty
        
        if 0 < total <= self._get_balance():
            self._set_balance(self._get_balance() - total)
            return f"Withdrew {amount} with a penalty of {penalty}. New balance is {self._get_balance()}."
        else:
            return f"Insufficient funds in Savings Account. Withdrawal amount {amount} plus penalty {penalty} must be positive and less than or equal to the current balance."
        
class PayrollAccount(BankAccount): # Inheritance
    def withdraw(self, amount):  # Polymorphism
        if 0 < amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
            return f"Withdrew {amount}. New balance is {self._get_balance()}."
        else:
            return f"Insufficient funds in Payroll Account. Withdrawal amount {amount}  must be positive and less than or equal to the current balance."
        
        
        
        
# account = BankAccount("Bastian", 1000)  # instantiation, Abstraction
savings_account = SavingsAccount("Bastian", 1000) 
payroll_account = PayrollAccount("Bastian", 1000)


print(savings_account.check_balance())
print(savings_account.deposit(500))
print(savings_account.deposit(0))
print(savings_account.deposit(-1))
print(savings_account.withdraw(200))
print(savings_account.withdraw(20000))
print(savings_account.withdraw(-10))
print(savings_account.check_balance())

print("\n")
print(payroll_account.check_balance())
print(payroll_account.deposit(500))
print(payroll_account.deposit(0))
print(payroll_account.deposit(-1))
print(payroll_account.withdraw(200))
print(payroll_account.withdraw(20000))
print(payroll_account.withdraw(-10))
print(payroll_account.check_balance())
