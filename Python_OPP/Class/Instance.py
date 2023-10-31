class Shop:
    shopping_mall = 'Jamuna'

    def __init__ (self, buyer):
        self.buyer = buyer 
        self.cart = []      # Cart is an instance attribute


    def add_to_cart(self, item):
        self.cart.append(item)


mahzabeein = Shop('Mehzabeen')

mahzabeein.add_to_cart("Shoes")
mahzabeein.add_to_cart("Phone")

print(mahzabeein.cart)


nisho = Shop("Nishi night er Nisho")
nisho.add_to_cart('Hat')
nisho.add_to_cart('Wath')

print(nisho.cart)


apurbo = Shop('Apurbo')
apurbo.add_to_cart('Chiruni')
apurbo.add_to_cart('Phone')

print(apurbo.cart)