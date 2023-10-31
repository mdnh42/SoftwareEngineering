

def call():
    print("Calling someone i dont know")
    return 'call done'


class PHone:

    price = 1200
    color = 'Blue'
    brand= 'samsung'
    feature = ['Camera', 'speaker', 'hammar']

    def call(self):
        print('calling one person')

    def sand_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message {sms}'
        return text
    
my_phone = PHone()
print(my_phone.brand)
print(my_phone.call())

result = my_phone.sand_sms(444, 'Hi')
print(result)