class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name 
        self.price = price 
    

    def move(self):
        pass 

    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()
    
class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight =weight
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()

class PickupTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

    def __repr__(self) -> str:
        return super().__repr__()

class ACBus(Bus):
    def __init__(self, name, price, seat, temparature) -> None:
        self.temparature = temparature
        super().__init__(name, price, seat)

    def __repr__(self, seat) -> str:
        print(f'{self.seat}')
        return super().__repr__()



green_line = ACBus('green', 500000, 22, 16)

print(green_line)