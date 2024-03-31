from singleton import DatabaseConnection
from abstract_factory.CreateInstitutionInterfaces import PublicInstitutionFactory, PrivateInstitutionFactory


def main():
    public_institution_factory = PublicInstitutionFactory()
    private_institution_factory = PrivateInstitutionFactory()

    while True:
        print("\n1. Establecer conexión a la base de datos")
        print("2. Crear Institución Pública")
        print("3. Crear Institución Privada")
        print("4. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            db_connection = DatabaseConnection()
            print(f"Estado de la conexión: {db_connection.connection}")

            # comprobando el patrón Singleton
            db_connection_2 = DatabaseConnection()
            print(db_connection is db_connection_2)

        elif option == "2":
            name = input("Ingrese el nombre de la Institución Pública: ")
            public_institution = public_institution_factory.create_institution(name)
            print(public_institution)

        elif option == "3":
            name = input("Ingrese el nombre de la Institución Privada: ")
            private_institution = private_institution_factory.create_institution(name)
            print(private_institution)

        elif option == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()