# Encapsulation restricts direct access to object data and protects it from unintended modifications.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance    # Private attribute (double underscore)
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount")
            
    def get_balance(self):
        return self.__balance

# Creating Object
account = BankAccount("John Doe", 1000)

account.deposit(500)  # Output: Deposited $500. New balance: $1500
print(account.get_balance())  # Output: 1500

# Accessing Private Attribute (Throws an error)
# print(account.__balance)  # AttributeError

# __balance is private (cannot be accessed outside the class).
# The get_balance method is used to retrieve the balance safely.