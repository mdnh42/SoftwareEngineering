def call():
    print("Calling someone i dont know")
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    feature = [
        'camera', 'speaker', 'hammer'
    ]
    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        print(f'sending SMS to: {phone} and message: {sms}')


my_phone = Phone()
print(my_phone.feature)
print(my_phone.feature)
my_phone.call()
result = my_phone.send_sms(4112, 'I forgot to miss you')
print(result)


 