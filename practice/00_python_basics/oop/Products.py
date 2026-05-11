
class Product:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def get_name(self):
        return self.product_name

    def set_name(self, name):
        self.product_name = name

p1 = Product("Laptop",258369)
print(p1.product_price)
print(p1.get_name())
p1.set_name("Tablet")
print(p1.get_name())

p2 = Product("Phone",12514785)
