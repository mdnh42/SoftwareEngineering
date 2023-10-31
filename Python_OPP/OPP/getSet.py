#Getter Setter and Read Only Property using property Decorator 


class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.__age = age 
        self.__money = money

    @property
    def age(self):
        return self.__age
    
    @property
    def salary(self):
        return self.__money
    
    def salary(self, value):
        if(value<0):
            return 'salary can not be negative'
        self.__money+=value

samu = User('Kopa', 21, 120000)

# print(samu.__money)
# print(samu.age())
print(samu.age)
print(samu.salary)