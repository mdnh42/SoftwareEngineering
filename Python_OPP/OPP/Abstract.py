from abc import ABC, abstractclassmethod
# Abstract base Class 

class Animal(ABC):
    @abstractclassmethod
    def eat(self):
        print('Hey Nana!, etaing banana')
    @abstractclassmethod
    def move(self):
        pass 

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.categrory = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print("Hey na nana, I eating baanna")
    def move(self):
        print("hanging on the banana")

layka = Monkey('lucky')
layka.eat()