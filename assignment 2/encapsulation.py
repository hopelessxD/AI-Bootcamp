class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited!!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Ram", 1000)
print("Owner:", account.owner)
print("Balance:", account.get_balance())
account.deposit(500)
print("Owner:", account.owner)
print("Balance:", account.get_balance())