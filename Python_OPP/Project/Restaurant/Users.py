from abc import ABC, abstractmethod
class User():
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone 
        self.email = email 
        self.address = address
    

class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        super().__init__(name, phone, email, address)
        self.wallet = money
        self.__order = None
        

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order
    

    def place_order(self, order):
        self.order = order
        print('f {self.name} placed an order {order.items}')

    def eat_food(self, order):
        print(f'{self.name} item food {order.items}')

    def pay_for_order(self, amount):
        pass 

    def give_trip(self, tips_amount):
        pass 

    def write_review(self, starts):
        pass 



class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department,
                 cooking_item) -> None:
        
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department =department
        self.cooking_item = cooking_item
        super().__init__(name, phone, email, address)

    def receive_salary(self):
        self.due = 0

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department, cooking_item)
        self.tips_earning = 0 

    def take_order(self, order):
        pass 

    def transfer_order(self, order):
        pass 

    def serve_food(self, order):
        pass 


    def receive_tips(self, amount):
        self.tips_earning += amount

    
class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department, cooking_item)
