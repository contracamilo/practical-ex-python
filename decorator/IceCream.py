class IceCream:
    def __init__(self, flavor, cost):
        self.flavor = flavor
        self.cost = cost

    def describe(self):
        return f"Helado de {self.flavor} (${self.cost})"