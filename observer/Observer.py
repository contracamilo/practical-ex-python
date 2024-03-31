class Observer:
    def update(self, subject):
        raise NotImplementedError("Subclasses must implement this method")
