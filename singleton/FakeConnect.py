class FakeConnect:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __str__(self):
        return f"Conectado a la base de datos '{self.database}' en el host '{self.host}' como el usuario '{self.user}'"