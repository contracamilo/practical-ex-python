from singleton import DatabaseConnection


def main():
    while True:
        print("\n1. Establecer conexión a la base de datos")
        print("2. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            db_connection = DatabaseConnection()
            print(f"Estado de la conexión: {db_connection.connection}")

            # comprobando el patrón Singleton
            db_connection_2 = DatabaseConnection()
            print(db_connection is db_connection_2)

        elif option == "2":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
