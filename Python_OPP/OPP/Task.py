class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}"


class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"{product.name} added to {self.shop_name}")
        else:
            print("Invalid product. Please provide a valid Product instance.")

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                print(f"Congratulations! You have successfully bought {product.name} from {self.shop_name}.")
                self.products.remove(product)
                return
        print(f"Sorry, {product_name} is not available in {self.shop_name}.")

    def display_products(self):
        print(f"Products available at {self.shop_name}:")
        for product in self.products:
            print(product)


# Example usage:

# Create products
product1 = Product(1, "Laptop", 1200.00)
product2 = Product(2, "Smartphone", 800.00)
product3 = Product(3, "Headphones", 50.00)

# Create a shop
my_shop = Shop("My Electronics Store")

# Add products to the shop using the add_product method
my_shop.add_product(product1)
my_shop.add_product(product2)
my_shop.add_product(product3)

# Display products in the shop
my_shop.display_products()

# Buy a product
my_shop.buy_product("Smartphone")

# Display updated products in the shop
my_shop.display_products()
