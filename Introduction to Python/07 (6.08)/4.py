class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"商品：{self.name}, 単価：{self.price:d}"


class Basket(dict):
    def add(self, other):
        if other not in self.keys():
            self[other] = 1
        else:
            self[other] += 1
        print(f"{other}　を買い物かごに入れました")

    def listing(self):
        for every_item in self.keys():
            print(f"{globals()[str(every_item)]} 数量：{self[every_item]:d}")

    def checkout(self):
        total = 0
        for every_item in self.keys():
            total += globals()[str(every_item)].price * self[every_item]
        self.listing()
        print(f"合計金額：{total:d}\n")


count = 1
print(f"***買い物かご{count:d},'END'を入力したら、会計します***")
shopping_list = Basket()
while True:
    x = str(input("品名を入力してください："))
    if x == "END":
        shopping_list.checkout()
        count += 1
        print(f"***買い物かご{count},'END'を入力したら、会計します***")
        shopping_list.clear()
    else:
        if str(x) not in vars():
            y = int(input(f"{x}　の価格を入力してください："))
            globals()[str(x)] = Product(x, y)
        shopping_list.add(x)
