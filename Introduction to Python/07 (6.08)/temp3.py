basket = {"1": "one", "2": "two"}


class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"


for i in range(1, 5):
    name = "apple" + str(i)
    locals()["product" + str(i)] = Product(name, i * 100)

print(type(locals()["product" + str(2)]))