class BankAccount:
    def __init__(self, initialAmount, acctName) -> None:
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\nAccount'{self.acctName}' created.\n Balance = ${self.balance}")

    def getBalance(self):
        print(f"\nAccount '{self.acctName}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\Deposit Complete")
        self.getBalance()