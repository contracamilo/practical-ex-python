class PublicInstitution:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Institución Pública: {self.name}"


class PrivateInstitution:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Institución Privada: {self.name}"
