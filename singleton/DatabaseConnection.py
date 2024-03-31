from singleton.FakeConnect import FakeConnect


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls.initialize_connection()
        return cls._instance

    @staticmethod
    def initialize_connection():
        connection = FakeConnect(
            host='hostname',
            user='username',
            password='password',
            database='database_name'
        )
        return connection
