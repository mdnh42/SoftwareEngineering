# poly --? many
# morph ---> Shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal makng some sound')


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Meow Meow")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Dgew")


don = Cat('Real Don')
don.make_sound()

shepared = Dog('Local ')
shepared.make_sound()