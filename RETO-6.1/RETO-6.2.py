# Función que verifica si una palabra es un palíndromo
def is_palindrome(word: str) -> bool:
    """
    Verifica si una palabra es un palíndromo.

    Args:
        word: Palabra ingresada por el usuario.

    Returns:
        True si la palabra es un palíndromo.
        False en caso contrario.

    Raises:
        ValueError:
            - Si la cadena está vacía.
            - Si la palabra contiene caracteres no válidos.
    """

    # Elimina espacios al inicio y final
    word = word.strip()

    # Verifica que la palabra no esté vacía
    if word == "":
        raise ValueError(
            "La palabra no puede estar vacía"
        )

    # Verifica que la palabra solo contenga letras
    if not word.isalpha():
        raise ValueError(
            "La palabra solo debe contener letras"
        )

    # Convierte la palabra a minúsculas
    word = word.lower()

    # Longitud de la palabra
    length: int = len(word)

    # Índice inicial
    start_index: int = 0

    # Índice final
    end_index: int = length - 1

    # Variable de control
    is_palindrome_word: bool = True

    # Recorre la palabra desde ambos extremos
    while start_index < end_index:

        start_letter: str = word[start_index]
        end_letter: str = word[end_index]

        # Verifica si las letras son diferentes
        if start_letter != end_letter:
            is_palindrome_word = False
            break

        # Avanza los índices
        start_index += 1
        end_index -= 1

    return is_palindrome_word


# ===================== MAIN =====================

try:

    # Solicita una palabra al usuario
    user_word: str = input(
        "Ingrese una palabra: "
    )

    # Ejecuta la validación
    result: bool = is_palindrome(user_word)

    # Muestra el resultado
    if result:
        print(
            "La palabra ingresada es un palíndromo."
        )

    else:
        print(
            "La palabra ingresada no es un palíndromo."
        )

# Captura errores de valor inválido
except ValueError as error:
    print(f"Error: {error}")

# Bloque que siempre se ejecuta
finally:
    print("Programa finalizado")