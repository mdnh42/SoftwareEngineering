class Shop:
    cart = [] # cart is a class attribute

    def __init__(self, buyer) :
        self.buyer = buyer


    def add_to_cart(self, item):
        self.cart.append(item)
        

mehzabeen = Shop('Meh Jabeen')
mehzabeen.add_to_cart('Shoes')
mehzabeen.add_to_cart('Phone')

print(mehzabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('Watch')

print(nisho.cart)