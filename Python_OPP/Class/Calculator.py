class Calculator:
    brand = 'Casio'
    
    def add(self, num1, num2):
        return num1 + num2
    
    def deduc(self, num1, num2):
        return num1 - num2


cal = Calculator()
result = cal.add(2,2)
print(result)
dedu = cal.deduc(5, 2)
print(dedu)
