# Función que verifica si un número es primo
def is_prime(number: int) -> bool:
    """
    Verifica si un número es primo.

    Args:
        number: Número entero a evaluar.

    Returns:
        True si el número es primo.
        False en caso contrario.
    """

    # Los números menores o iguales a 1 no son primos
    if number <= 1:
        return False

    # Primer divisor a evaluar
    divisor: int = 2

    # Verifica divisores hasta la raíz cuadrada del número
    while divisor * divisor <= number:

        # Si el número es divisible, no es primo
        if number % divisor == 0:
            return False

        divisor += 1

    return True


# Función que obtiene los números primos de una lista
def get_primes(number_list: list[int]) -> list[int]:
    """
    Obtiene todos los números primos de una lista.

    Args:
        number_list: Lista de números enteros.

    Returns:
        Lista con los números primos.
    """

    # Lista donde se almacenarán los números primos
    prime_list: list[int] = []

    # Recorre la lista de números
    for number in number_list:

        # Agrega el número si es primo
        if is_prime(number):
            prime_list.append(number)

    return prime_list


# ===================== MAIN =====================

try:

    # Solicita números separados por coma
    user_input: str = input(
        "Ingrese números separados por coma "
        "(ej: 4,7,9,11,15): "
    )

    # Verifica que la entrada no esté vacía
    if user_input.strip() == "":
        raise ValueError(
            "La entrada no puede estar vacía"
        )

    # Convierte los valores ingresados a enteros
    number_list: list[int] = [
        int(number.strip())
        for number in user_input.split(",")
    ]

    # Obtiene los números primos
    result: list[int] = get_primes(number_list)

    # Muestra resultados
    print(f"Lista original: {number_list}")
    print(f"Números primos: {result}")

# Captura errores de conversión o entrada inválida
except ValueError as error:
    print(f"Error: {error}")

# Bloque que siempre se ejecuta
finally:
    print("Programa finalizado")