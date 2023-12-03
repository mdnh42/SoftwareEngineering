class Product:
    def __init__(self, name, price, quantity) -> None:
        self.product_name  = name 
        self.product_price = price 
        self.product_quantity = quantity

class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity = {} 

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)

        self.__product_price[product.product_name] = product.product_price
        self.__product_quantity[product.product_name] = product.product_quantity

    def buy_product(self, name, quantity):
        if name in self.__product_price:
             if self.__product_quantity[name] >= quantity:
                self.__product_quantity[name] = self.__product_quantity[name] - quantity
                print('thank you')
             else:
                print('Unavaiable')
        else:
            print("No Found")

    def show_product(self):
        print(f'all products Price ', self.__product_price)
        print(f'all products Price ', self.__product_quantity)
        
class Shop(Store):
    def __init__(self, name) -> None:
        self.shop_name = name 
        super().__init__()


shop1 = Shop('Gadget 420')
shop1.add_product('Iphone', 20, 10)

shop1.__product_quantity = {}

# shop1.show_product()

shop1.buy_product('Iphone', 2)

# print(shop1.__product_price)
# print(shop1.__product_price)

