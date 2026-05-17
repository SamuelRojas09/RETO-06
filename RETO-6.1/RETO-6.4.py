# Función que calcula la mayor suma consecutiva
def max_consecutive_sum(number_list: list[int]) -> int:
    """
    Calcula la mayor suma entre dos números consecutivos
    de una lista.

    Args:
        number_list: Lista de números enteros.

    Returns:
        Mayor suma consecutiva.

    Raises:
        ValueError:
            Si la lista tiene menos de dos elementos.
    """

    # Verifica que la lista tenga al menos dos números
    if len(number_list) < 2:
        raise ValueError(
            "La lista debe contener al menos dos números"
        )

    # Suma inicial de los dos primeros números
    current_sum: int = (
        number_list[0] + number_list[1]
    )

    # La suma máxima inicia con la primera suma
    max_sum: int = current_sum

    # Índice inicial
    index: int = 1

    # Recorre la lista
    while index < len(number_list) - 1:

        current_number: int = number_list[index]
        next_number: int = number_list[index + 1]

        # Calcula suma consecutiva
        current_sum = (
            current_number + next_number
        )

        # Actualiza la suma máxima
        if current_sum > max_sum:
            max_sum = current_sum

        index += 1

    return max_sum


# ===================== MAIN =====================

while True:

    try:

        # Solicita los números al usuario
        user_input: str = input(
            "Ingrese los números separados "
            "por espacios: "
        )

        # Verifica que la entrada no esté vacía
        if user_input.strip() == "":
            raise ValueError(
                "La entrada no puede estar vacía"
            )

        # Convierte los números ingresados
        numbers: list[int] = [
            int(number)
            for number in user_input.split()
        ]

        # Ejecuta la función
        result: int = max_consecutive_sum(
            numbers
        )

        # Muestra el resultado
        print(
            "La mayor suma consecutiva es:",
            result
        )

        # Sale del ciclo si todo salió bien
        break

    # Captura errores de valor inválido
    except ValueError as error:
        print(f"Error: {error}")

    # Bloque que siempre se ejecuta
    finally:
        print("Intento finalizado")