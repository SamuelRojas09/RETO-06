# Función que agrupa palabras con los mismos caracteres
def words_with_same_characters(
    word_list: list[str]
) -> list[list[str]]:
    """
    Agrupa palabras que contienen
    exactamente los mismos caracteres.

    Args:
        word_list: Lista de palabras.

    Returns:
        Lista de grupos de palabras
        con los mismos caracteres.

    Raises:
        TypeError:
            Si algún elemento no es texto.

        ValueError:
            Si una palabra contiene
            caracteres no válidos.
    """

    # Verifica que la lista no esté vacía
    if len(word_list) == 0:
        raise ValueError(
            "La lista no puede estar vacía."
        )

    # Validación de palabras
    for word in word_list:

        # Verifica que sea texto
        if not isinstance(word, str):
            raise TypeError(
                "Todos los elementos deben ser texto."
            )

        # Elimina espacios
        clean_word: str = word.strip()

        # Verifica que no esté vacía
        if clean_word == "":
            raise ValueError(
                "Las palabras no pueden estar vacías."
            )

        # Verifica que solo tenga letras
        if not clean_word.isalpha():
            raise ValueError(
                "Las palabras solo deben contener letras."
            )

    # Lista resultado
    result: list[list[str]] = []

    # Lista para controlar palabras usadas
    used: list[bool] = [False] * len(word_list)

    # Índice principal
    index: int = 0

    while index < len(word_list):

        if used[index]:
            index += 1
            continue

        # Palabra base
        base_word: str = word_list[index].lower()

        # Letras ordenadas
        base_letters: list[str] = sorted(base_word)

        # Grupo actual
        group: list[str] = [word_list[index]]

        used[index] = True

        # Comparación con las demás palabras
        other_index: int = index + 1

        while other_index < len(word_list):

            if not used[other_index]:

                current_word: str = (
                    word_list[other_index].lower()
                )

                current_letters: list[str] = sorted(
                    current_word
                )

                are_equal: bool = True

                # Verifica tamaño
                if len(base_letters) != len(
                    current_letters
                ):
                    are_equal = False

                else:
                    position: int = 0

                    while position < len(base_letters):

                        if (
                            base_letters[position]
                            != current_letters[position]
                        ):
                            are_equal = False
                            break

                        position += 1

                # Si tienen las mismas letras
                if are_equal:
                    group.append(
                        word_list[other_index]
                    )

                    used[other_index] = True

            other_index += 1

        # Solo agrega grupos con más de una palabra
        if len(group) > 1:
            result.append(group)

        index += 1

    return result


# ===================== MAIN =====================

try:

    # Solicita palabras al usuario
    user_input: str = input(
        "Ingrese palabras separadas por espacios: "
    )

    # Elimina espacios extremos
    user_input = user_input.strip()

    # Verifica que no esté vacío
    if user_input == "":
        raise ValueError(
            "Debe ingresar al menos una palabra."
        )

    # Divide las palabras
    parts: list[str] = user_input.split()

    # Lista final
    words: list[str] = []

    # Recorre palabras
    position: int = 0

    while position < len(parts):

        word: str = parts[position]

        # Agrega palabra
        words.append(word)

        position += 1

    # Ejecuta la función
    result: list[list[str]] = (
        words_with_same_characters(words)
    )

    # Muestra resultados
    if len(result) == 0:
        print(
            "No se encontraron palabras "
            "con los mismos caracteres."
        )

    else:
        for group in result:
            print(
                "Palabras con los mismos caracteres:",
                group
            )

# Error de valor inválido
except ValueError as error:
    print(f"Error: {error}")

# Error de tipo inválido
except TypeError as error:
    print(f"Error: {error}")

# Captura cualquier otro error
except Exception as error:
    print(f"Error inesperado: {error}")

# Bloque final
finally:
    print("Programa finalizado.")