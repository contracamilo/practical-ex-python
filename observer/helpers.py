def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, introduce un número válido.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Por favor, introduce un valor no vacío.")
