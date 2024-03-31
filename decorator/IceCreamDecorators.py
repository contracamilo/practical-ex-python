from decorator import IceCream


class IceCreamDecorator(IceCream):
    def __init__(self, ice_cream, flavor, cost):
        super().__init__(flavor, cost)
        self._ice_cream = ice_cream

    def describe(self):
        return self._ice_cream.describe()


class ToppingDecorator(IceCreamDecorator):
    def __init__(self, ice_cream, topping, topping_cost=0.75):
        super().__init__(ice_cream, ice_cream.flavor, ice_cream.cost)
        self.topping = topping
        self.topping_cost = topping_cost

    def describe(self):
        return f"{self._ice_cream.describe()} con {self.topping} (+${self.topping_cost})"

    def get_cost(self):
        return self._ice_cream.get_cost() + self.topping_cost


class SauceDecorator(IceCreamDecorator):
    def __init__(self, ice_cream, sauce, sauce_cost=0.50):
        super().__init__(ice_cream, ice_cream.flavor, ice_cream.cost)
        self.sauce = sauce
        self.sauce_cost = sauce_cost

    def describe(self):
        return f"{self._ice_cream.describe()} con salsa de {self.sauce} (+${self.sauce_cost})"

    def get_cost(self):
        return self._ice_cream.get_cost() + self.sauce_cost
