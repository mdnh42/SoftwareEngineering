class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    


    def deposit(self, amount):
        if(amount>0):
            self.balance += amount
        
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print( f'Fokira. You can withdraw below{self.min_withdraw}')
        elif amount>self.max_withdraw:
            print (f'Bank fokir hoye jabe. You can not with more then {self.max_withdraw}')
        else:
            self.balance -= amount
            print (f'here is your money {amount}')


brac = Bank("150000")
brac.withdraw(25)
brac.withdraw(500000)
print()

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(5000)

print()