from singleton import DatabaseConnection
from abstract_factory.CreateInstitutionInterfaces import PublicInstitutionFactory, PrivateInstitutionFactory
from adapter.TranslatorAdapter import TranslatorAdapter


def main():
    # Patron Abstract factory
    public_institution_factory = PublicInstitutionFactory()
    private_institution_factory = PrivateInstitutionFactory()

    # Patron Adapter
    translate_adapter = TranslatorAdapter()

    while True:
        print("\n1. Establecer conexión a la base de datos")
        print("2. Crear Institución Pública")
        print("3. Crear Institución Privada")
        print("4. Traducir texto")
        print("5. Salir")
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
            text = input("Ingresa el texto 'Hola mundo' para traducir: ")
            if text != "Hola mundo":
                print("Error: El texto ingresado no es 'Hola mundo'")
            else:
                target_language = input(
                    "Ingrese el idioma objetivo (en para inglés, pt para portugués, fr para francés): ")
                translation = translate_adapter.translate(text, target_language)
                print(f"Traducción: {translation}")

        elif option == "5":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
