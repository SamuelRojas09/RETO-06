# Función que realiza operaciones matemáticas básicas
def operations(number_1: int, number_2: int, character: str) -> float | int:
    """
    Realiza una operación matemática básica entre dos números.

    Args:
        number_1: Primer número.
        number_2: Segundo número.
        character: Operador matemático (+, -, *, /).

    Returns:
        Resultado de la operación.

    Raises:
        ZeroDivisionError: Si se intenta dividir entre cero.
        ValueError: Si el operador ingresado es inválido.
    """

    # Operación de suma
    if character == "+":
        return number_1 + number_2

    # Operación de resta
    if character == "-":
        return number_1 - number_2

    # Operación de multiplicación
    if character == "*":
        return number_1 * number_2

    # Operación de división
    if character == "/":

        # Validación de división entre cero
        if number_2 == 0:
            raise ZeroDivisionError(
                "No se puede dividir entre cero"
            )

        return number_1 / number_2

    # Excepción para operadores inválidos
    raise ValueError(
        "Ingreso un caracter invalido"
    )


# ===================== MAIN =====================

try:
    # Solicita el primer número
    number_1: int = int(
        input("Ingrese el primer numero: ")
    )

    # Solicita el segundo número
    number_2: int = int(
        input("Ingrese el segundo numero: ")
    )

    # Solicita el operador
    character: str = input(
        "Ingrese el signo de la operación (+, -, *, /): "
    )

    # Ejecuta la operación
    result: float = operations(
        number_1,
        number_2,
        character
    )

    # Muestra el resultado
    print(f"Resultado: {result}")

# Captura errores de valores inválidos
except ValueError as error:
    print(f"Error: {error}")

# Captura errores de división entre cero
except ZeroDivisionError as error:
    print(f"Error: {error}")

# Bloque que siempre se ejecuta
finally:
    print("Programa finalizado")
