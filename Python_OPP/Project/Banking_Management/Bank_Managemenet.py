class User:
    user_list = []
    def __init__(self,name,phone,password,balance,loan):
        self.name = name
        self.phone = phone
        self.password = password
        self.balance = balance
        self.loan = loan
        self.transaction = []

        User.user_list.append(vars(self))


class Admin:
    admin_list = []
    def __init__(self,name,phone,password):
        self.name = name
        self.phone = phone
        self.password = password

        Admin.admin_list.append(vars(self))



class Bank:
    bank_balance = 0
    loan_balance = 0
    loan_enable = True

    def loan_switch_on(self):
        self.loan_enable = True

    def loan_switch_off(self):
        self.loan_enable = False

    def total_balance(self):
        print(f"Total bank balance is : {self.bank_balance} BDT")

    def total_loan(self):
        print(f"Total loan balance is {self.loan_balance} BDT")


class UserAccount(User):
    def __init__(self, name, phone, password):
        super().__init__(name, phone, password, balance=0,loan=0)
        

    def deposit(self,user):
        print()
        amount = int(input("Enter your depositable amount : "))
        if amount >= 0:
            user['balance'] += amount
            user['transaction'].append(f"Deposited : {amount} BDT")
            bank.bank_balance += amount
        else:
            print("Invalid amount.")
    
    def withdraw(self,user):
        print()
        if user['balance'] > 0:
            amount = int(input("Enter your withdrawal amount : "))

            if amount >=0 and amount <= user['balance']:
                if bank.bank_balance > 0 and bank.bank_balance >= amount:
                    user['balance'] -= amount
                    user['transaction'].append(f"Withdrawal : {amount} BDT")
                    bank.bank_balance -= amount
                    print(f"Successfully withdrawal {amount} BDT, thank you.")
                else:
                    print("The bank is bankrupt.")
            else:
                print("Invalid amount.")
        else:
            print("You don't have balance")
    
    def balance_check(self,user):
        print(f"Your balance is : {user['balance']} BDT")

    def transfer(self,my_self):
        print()
        if my_self['balance'] > 0:
            name = input("Enter transferring account name : ")
            phone = input("Enter transferring account phone number : ")

            flag = 1
            for user in self.user_list:
                if user['name'] == name and user['phone'] == phone:
                    flag = 0
                    amount = int(input("Enter transferring amount : "))
                    print()
                    if  amount >= 0 and amount <= my_self['balance']:
                        my_self['balance'] -= amount
                        my_self['transaction'].append(f"Transferred : {amount} BDT to {user['name']}")
                        user['balance'] += amount
                        user['transaction'].append(f"Received : {amount} BDT from {my_self['name']}")
                        print(f"Successfully transferred {amount} BDT to {user['name']}")
                    else:
                        print("Invalid amount.")
            if flag:
                print("No user found.")
        else:
            print("You don't have balance")

    def trans_history(self,user):
        print(f"\n<-----------Hi {user['name']}, Your transaction history----------->")
        for val in user['transaction']:
            print(val)
        print("<---------------------End history------------------------->")

    def take_loan(self,user):
        print()
        if bank.loan_enable == True:
            if user['balance'] > 0:
                limit = user['balance']*2
                print(f"Availabe elligible loan amount for you : {limit} BDT\n")
                amount = int(input("Please enter the loan amount you wish to receive : "))
                if amount >= 0 and amount <= limit:
                    if bank.bank_balance >= amount:
                        user['loan'] += amount
                        bank.loan_balance += amount
                        bank.bank_balance -= amount
                        user['transaction'].append(f"Loan : {amount} BDT from Bank")
                        print(f"Here's your loan money : {amount} BDT")
                    else:
                        print("Bank dosen't have sufficient money.")
                else:
                    print("Invalid amount")
            else:
                print("Your'e not elligible for loan")
        else:
            print("Loan services is off.")
    

    def loan_balance(self,user):
        print(f"Your total loan is : {user['loan']} BDT")


    def pay_loan(self,user):
        print(f"\nYour balance is : {user['balance']}")
        print(f"Your loan balance is : {user['loan']}\n")
        if user['loan'] > 0:
            if user['balance'] >= user['loan']:
                user['balance'] -= user['loan']
                bank.loan_balance -= user['loan']
                user['transaction'].append(f"Repay loan : {user['loan']} BDT to Bank")
                user['loan'] = 0
                print(f"After repay loan, your balance is : {user['balance']} BDT")
            else:
                print("You don't have sufficient balance to repay loan.")
        else:
            print("You don't have loan to pay.")


class AdminAccount(Admin):
    def __init__(self, name, phone, password):
        super().__init__(name, phone, password)
    

bank = Bank()
while True:
    print("\n<>----------Welcome to the our Banking Managment System----------<>\n")
    print("1. User")
    print("2. Admin")
    print("3. Quit\n")

    choice = int(input("Enter your choice : "))
    if choice == 3:
        break
    elif choice == 1:
        while True:
            print("\n<..........Wellcome to the user interface...........>\n")
            print("1. Create account")
            print("2. Login")
            print("3. Back\n")

            a = int(input("Enter your choice : "))
            if a == 3:
                break
            elif a == 1:
                name = input("\nEnter your account name : ")
                phone = input("Enter your phone number : ")
                password = input("Enter your password : ")
                print()
    
                user_ac = UserAccount(name, phone, password)
                print("User account created successfully.")
            elif a == 2:
                phone = input("\nEnter your account phone number : ")
                password = input("Enter your account password : ")
                
                flag = 1
                f = 0
                for user in user_ac.user_list:
                    if user['phone'] == phone and user['password'] == password:
                        flag = 0
                        while True:
                            print(f"\n<>...Wellcome {user['name']}, to our Banking system...<>\n")
                            print("1. Deposit")
                            print("2. Withdraw")
                            print("3. Balance Check")
                            print("4. Transfer")
                            print("5. Transaction History")
                            print("6. Take Loan")
                            print("7. Loan Check")
                            print("8. Repay Loan")
                            print("9. Logout\n")

                            b = int(input("Enter your choice : "))
                            if b == 9:
                                f = 1
                                break
                            elif b == 1:
                                user_ac.deposit(user)
                                print("Successfully deposited.")
                            elif b == 2:
                                user_ac.withdraw(user)
                            elif b == 3:
                                user_ac.balance_check(user)
                            elif b == 4:
                                user_ac.transfer(user)
                            elif b == 5:
                                user_ac.trans_history(user)
                            elif b == 6:
                                user_ac.take_loan(user)
                            elif b == 7:
                                user_ac.loan_balance(user)
                            elif b == 8:
                                user_ac.pay_loan(user)
                            else:
                                print("Invalid choice.")
                        if f:
                            break
                if flag:
                    print("\nNo user found.")            
            else:
                print("\nInvalid choice.")
    
    elif choice == 2:
        while True:
            print("\n<..........Wellcome to the admin interface...........>\n")
            print("1. Create account")
            print("2. Login")
            print("3. Back\n")

            c = int(input("Enter your choice : "))
            if c == 3:
                break
            elif c == 1:
                name = input("\nEnter your account name : ")
                phone = input("Enter your phone number : ")
                password = input("Enter your password : ")
                print()

                admin_ac = AdminAccount(name, phone, password)
                print("Admin account created successfully.")
            elif c == 2:
                phone = input("\nEnter your account phone number : ")
                password = input("Enter your account password : ")

                flag = 1
                f = 0
                for val in admin_ac.admin_list:
                    if val['phone'] == phone and val['password'] == password:
                        flag = 0
                        while True:
                            print(f"\n<>...Wellcome {val['name']}, to our Banking system...<>\n")
                            print("1. Total Balance")
                            print("2. Total Loan")
                            print("3. Loan System Change")
                            print("4. Logout\n")

                            d = int(input("Enter your choice : "))
                            if d == 4:
                                f = 1
                                break
                            elif d == 1:
                                bank.total_balance()
                            elif d == 2:
                                bank.total_loan()
                            elif d == 3:
                                print("<>----Loan services feature----<>\n")
                                print("1. Loan Service On")
                                print("2. Loan Service Off\n")

                                e = int(input("Enter your choice : "))
                                if e == 1:
                                    bank.loan_switch_on()
                                    print("Loan service has been on.")
                                elif e == 2:
                                    bank.loan_switch_off()
                                    print("Loan service has been off.")
                                else:
                                    print("Invalid choice.")
                            else:
                                print("Invalid choice")
                        if f:
                            break
                if flag:
                    print("\nNo admin found.")
    else:
        print("\nInvalid choice.")
        