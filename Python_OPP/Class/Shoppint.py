class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price' : price, 'quantity' : quantity }
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total+=item['price'] * item['quantity']
        
        print('Total Price', total)
        if amount <total:
            print(f'Please provide {total - amount} more')
        else:
            extrat = amount - total
            print(f'Here is extra{extrat}')
alanSopon = Shopping('Alan Shopon')
alanSopon.add_to_cart('Alo', 50, 6)
alanSopon.add_to_cart('Dim', 12, 12)
alanSopon.add_to_cart('Rice', 50, 5)


print(alanSopon.cart)
alanSopon.checkout(600)
alanSopon.checkout(1600)
