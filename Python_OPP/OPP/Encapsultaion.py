class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.initial_deposit = initial_deposit
        self.__balance = initial_deposit

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    

    def withdraw(self, amount):
        if amount<self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Khali'

rafsun = Bank('Chotoo bro', 1000) 
print(rafsun.holder_name)
rafsun.deposit(40000)
print(rafsun.get_balance())