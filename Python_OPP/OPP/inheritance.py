#base Class / Parent Class / Common attribute + functionality class 
# derived class , child class, uncommon attribute + functionality class 

class Device:
    def __init__(self, brand, price, color, origin) -> None:    
        self.brand = brand 
        self.price = price 
        self.color = color 
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'
    

class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory
        
    def coding(self):
        return f'Learning python and Practicing'
    

class Phone(Device): 
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim =dual_sim
        super().__init__(brand, price, color, origin)

    def call(self, number, text):
        return f'sending SMS to: {number}: {text}'
    
    def __repr__(self) -> str:
        return f'Phone:{self.dual_sim}'


class Camera:
    def __init__(self,  pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass 



# Inheritance 

my_phone = Phone('Iphone', 12000, 'Silver', 'China', True)
print(my_phone.brand)
print(my_phone)
