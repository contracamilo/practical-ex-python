from observer import Observer


class PriceAlert(Observer):
    def __init__(self, threshold):
        self.threshold = threshold

    def update(self, product):
        if product.price < self.threshold:
            print(f"Alerta: El precio de {product.name} ha caído por debajo de {self.threshold}")
