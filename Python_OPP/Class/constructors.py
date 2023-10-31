class Phone: 
    manufactured = 'China'

    def __init__(self,owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_sm(self, phone, sms):
        text = f'Sendingto {phone} {sms}'
        print(text)


my_phone  = Phone('Kala Chan', 'Oppo', 8500)
my_phone2  = Phone('Kala Chan', 'Oppo', 8500)

print(my_phone.owner, my_phone.brand, my_phone.price)
print(my_phone2.owner, my_phone2.brand, my_phone2.price)

my_phone3 = Phone('HI', 'How Are  YOu')

print()