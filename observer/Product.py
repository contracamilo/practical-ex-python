from observer import Subject


class Product(Subject):
    def __init__(self, name, price):
        super().__init__()
        self.name = name
        self.price = price

    def set_price(self, price):
        self.price = price
        print(f"El precio de {self.name} ha sido actualizado a {self.price}")
        self.notify()
