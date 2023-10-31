class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age 
        self.height = height
        self.weight = weight

    def eat(self):
        print("vat mangso polau korma")

    def excerise(self):
        raise NotImplementedError


class Circketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    #Override 
    def eat(self):
        print('Vegetable')

    def excerise(self):
        print("gym")

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.age * other.age
    
    def __len__(self):
        return self.height + self.height
    
    def __gt__(self, other):
        return self.height > other.height

sakib = Circketer('Sakib', 38, 68, 91, 'BD')
# sakib.eat()
# sakib.excerise()


print(45+63)
print('Sakib' + 'Rakib')
print([12, 9800] + [252 , 52])

mushi = Circketer('Mushi', 65, 41, 65, 'BD')
print(sakib + mushi)
print(sakib * mushi)

print(len(sakib))

print(sakib > mushi)
