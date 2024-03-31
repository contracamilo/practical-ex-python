from decorator import IceCream, ToppingDecorator, SauceDecorator
from observer import Product, PriceAlert, get_non_empty_input, get_float_input
from singleton import DatabaseConnection
from abstract_factory.CreateInstitutionInterfaces import PublicInstitutionFactory, PrivateInstitutionFactory
from adapter.TranslatorAdapter import TranslatorAdapter


def main():
    # Patrón Abstract factory
    public_institution_factory = PublicInstitutionFactory()
    private_institution_factory = PrivateInstitutionFactory()

    # Patrón Adapter
    translate_adapter = TranslatorAdapter()

    # Patrón Observer
    product = None

    while True:
        print("\n1. Establecer conexión a la base de datos")
        print("2. Crear Institución Pública")
        print("3. Crear Institución Privada")
        print("4. Traducir texto")
        print("5. Crear helado personalizado")
        print("6. Crear producto y configurar alertas de precios")
        print("7. Cambiar precio del producto")
        print("8. Salir")
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
            flavor = input("Ingrese el sabor del helado: ")
            while not flavor:
                print("Error: El sabor del helado no puede estar vacío. Por favor, intente de nuevo.")
                flavor = input("Ingrese el sabor del helado: ")

            ice_cream = IceCream(flavor, 2.50)
            add_topping = input("¿Desea agregar un topping? (s/n): ")

            if add_topping.lower() == 's':
                topping = input("Ingrese el topping: ")
                ice_cream = ToppingDecorator(ice_cream, topping)

            add_sauce = input("¿Desea agregar salsa? (s/n): ")

            if add_sauce.lower() == 's':
                sauce = input("Ingrese la salsa: ")
                ice_cream = SauceDecorator(ice_cream, sauce)

            print(ice_cream.describe())

        elif option == "6":
            product_name = get_non_empty_input("Ingrese el nombre del producto: ")
            product_price = get_float_input("Ingrese el precio del producto: ")
            product = Product(product_name, product_price)

            alert1_threshold = get_float_input("Ingrese el valor máximo para la primera alerta de precio: ")
            alert2_threshold = get_float_input("Ingrese el valor máximo la segunda alerta de precio: ")

            alert1 = PriceAlert(alert1_threshold)
            alert2 = PriceAlert(alert2_threshold)

            product.attach(alert1)
            product.attach(alert2)

            print(f"Producto {product_name} creado y alertas de precios configuradas.")

        elif option == "7":
            if product is None:
                print("Primero debes crear un producto.")
            else:
                try:
                    new_price = float(input("Introduce el nuevo precio del producto: "))
                    product.set_price(new_price)
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif option == "8":
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
