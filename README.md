# Reto 6.1 - Manejo de Excepciones del Reto 1

## Descripción

En este reto se agregaron excepciones a los programas desarrollados en el Reto 1, siguiendo el estándar PEP 8.

El objetivo fue validar entradas incorrectas, prevenir errores durante la ejecución y manejar situaciones inesperadas utilizando:

- `try`
- `except`
- `finally`
- `raise`

---

# 1. Calculadora de Operaciones Básicas

## Excepciones agregadas

### `ZeroDivisionError`

Se agregó esta excepción para evitar divisiones entre cero.

```python
if number_2 == 0:
    raise ZeroDivisionError(
        "No se puede dividir entre cero"
    )
```

### `ValueError`

Se agregó cuando el operador ingresado no es válido.

```python
raise ValueError(
    "Ingreso un caracter invalido"
)
```

## Manejo de excepciones

```python
except ValueError as error:
    print(f"Error: {error}")

except ZeroDivisionError as error:
    print(f"Error: {error}")
```

## ¿Qué mejora aporta?

- Evita errores matemáticos inválidos.
- Informa claramente al usuario.
- Mantiene el programa funcionando correctamente.

---

# 2. Verificador de Palíndromos

## Excepciones agregadas

### `ValueError` por cadena vacía

```python
if word == "":
    raise ValueError(
        "La palabra no puede estar vacía"
    )
```

### `ValueError` por caracteres inválidos

```python
if not word.isalpha():
    raise ValueError(
        "La palabra solo debe contener letras"
    )
```

## Manejo de excepciones

```python
except ValueError as error:
    print(f"Error: {error}")
```

## ¿Qué mejora aporta?

- Evita entradas vacías.
- Impide números o símbolos.
- Garantiza que la validación del palíndromo sea correcta.

---

# 3. Lista de Números Primos

## Excepciones agregadas

### `ValueError` por entrada vacía

```python
if user_input.strip() == "":
    raise ValueError(
        "La entrada no puede estar vacía"
    )
```

### `ValueError` por conversión inválida

```python
number_list: list[int] = [
    int(number.strip())
    for number in user_input.split(",")
]
```

Si el usuario escribe texto no numérico, Python genera automáticamente un `ValueError`.

## Manejo de excepciones

```python
except ValueError as error:
    print(f"Error: {error}")
```

## ¿Qué mejora aporta?

- Evita listas vacías.
- Evita caracteres inválidos.
- Garantiza que solo se procesen números enteros.

---

# 4. Mayor Suma Consecutiva

## Excepciones agregadas

### `ValueError` por lista insuficiente

```python
if len(number_list) < 2:
    raise ValueError(
        "La lista debe contener al menos dos números"
    )
```

### `ValueError` por entrada vacía

```python
if user_input.strip() == "":
    raise ValueError(
        "La entrada no puede estar vacía"
    )
```

### `ValueError` por conversión inválida

```python
numbers: list[int] = [
    int(number)
    for number in user_input.split()
]
```

## Manejo de excepciones

```python
except ValueError as error:
    print(f"Error: {error}")
```

## ¿Qué mejora aporta?

- Evita operaciones inválidas.
- Garantiza que existan suficientes números.
- Previene errores de conversión.

---

# 5. Agrupación de Palabras con los Mismos Caracteres

## Excepciones agregadas

### `ValueError` por lista vacía

```python
if len(word_list) == 0:
    raise ValueError(
        "La lista no puede estar vacía."
    )
```

### `TypeError` por elementos no texto

```python
if not isinstance(word, str):
    raise TypeError(
        "Todos los elementos deben ser texto."
    )
```

### `ValueError` por palabras vacías

```python
if clean_word == "":
    raise ValueError(
        "Las palabras no pueden estar vacías."
    )
```

### `ValueError` por caracteres inválidos

```python
if not clean_word.isalpha():
    raise ValueError(
        "Las palabras solo deben contener letras."
    )
```

## Manejo de excepciones

```python
except ValueError as error:
    print(f"Error: {error}")

except TypeError as error:
    print(f"Error: {error}")

except Exception as error:
    print(f"Error inesperado: {error}")
```

## ¿Qué mejora aporta?

- Valida correctamente las palabras.
- Evita entradas inválidas.
- Permite manejar errores inesperados.

---

# Conclusiones

Con la implementación de excepciones se logró:

- Mejorar la robustez de los programas.
- Validar entradas incorrectas.
- Evitar errores matemáticos y lógicos.
- Mostrar mensajes claros al usuario.
- Mantener la ejecución controlada.

Todos los programas fueron desarrollados utilizando:
- Comentarios descriptivos
- Estándar PEP 8
- Manejo adecuado de excepciones


# Reto 6.2 - Manejo de Excepciones en el paquete Shape

## Descripción

En este reto se agregaron excepciones al paquete `Shape` para mejorar la validación de datos y evitar errores matemáticos o geométricos durante la ejecución del programa.

Las excepciones fueron implementadas siguiendo:

- Reglas de estilo PEP 8.
- Uso de tipado estático con `typing`.
- Manejo adecuado de errores mediante `raise`.

---

# Excepciones implementadas

## 1. Excepción en `Line`

### Problema

Una línea no puede construirse usando dos puntos idénticos, ya que su longitud sería cero.

### Solución

Se agregó una validación en el constructor de `Line` para verificar que el punto inicial y el final sean diferentes.

### Código agregado

```python
if (
    start.get_x() == end.get_x()
    and start.get_y() == end.get_y()
):
    raise ValueError(
        "A line cannot have identical points."
    )
```

### ¿Qué evita?

- Segmentos inválidos.
- Errores geométricos posteriores.
- Longitudes iguales a cero.

---

## 2. Excepción en `Triangle`

### Problema

Un triángulo debe tener exactamente 3 vértices.

Además, los puntos no pueden estar alineados, porque eso no forma un triángulo válido y puede generar errores matemáticos en:

- Fórmula de Herón.
- Ley de cosenos.
- Cálculo de ángulos.

### Solución

Se agregaron dos validaciones.

### Validación de cantidad de vértices

```python
if len(vertices) != 3:
    raise ValueError(
        "A triangle must have exactly 3 vertices."
    )
```

### Validación de triángulo válido

```python
if self.compute_area() == 0:
    raise ValueError(
        "The vertices do not form a valid triangle."
    )
```

### ¿Qué evita?

- Triángulos inválidos.
- Errores matemáticos.
- Problemas en el cálculo de ángulos y área.

---

## 3. Excepción en `Square`

### Problema

Un cuadrado debe tener sus cuatro lados iguales.

Si no se valida esto, podrían crearse figuras incorrectas usando la clase `Square`.

### Solución

Se verificó que todos los lados tengan la misma longitud.

### Código agregado

```python
for side in sides:
    if abs(side - first) > 1e-6:
        raise ValueError("Not a square")
```

### ¿Qué evita?

- Crear rectángulos usando la clase `Square`.
- Resultados geométricos incorrectos.
- Inconsistencias en la herencia.

---

## 4. Excepción en `Rectangle`

### Problema

Un rectángulo debe tener exactamente 4 vértices.

Si se ingresan más o menos puntos, la figura no puede construirse correctamente.

### Solución

Se agregó una validación para comprobar que el número de vértices sea exactamente 4.

### Código agregado

```python
if len(vertices) != 4:
    raise ValueError(
        "A rectangle must have exactly 4 vertices."
    )
```

### ¿Qué evita?

- Construcción incorrecta de rectángulos.
- Errores al crear los lados.
- Problemas en el cálculo de área y perímetro.

---

## 5. Excepción en `Equilateral`

### Problema

Un triángulo equilátero debe tener sus tres lados iguales.

Si no se valida esta condición, podrían crearse triángulos incorrectos usando la clase `Equilateral`.

### Solución

Se utilizó el método `is_regular()` para verificar que el triángulo realmente sea equilátero.

### Código agregado

```python
if not self.is_regular():
    raise ValueError(
        "Not an equilateral triangle"
    )
```

### ¿Qué evita?

- Crear triángulos no equiláteros.
- Inconsistencias en la jerarquía de clases.
- Errores geométricos en figuras especiales.

---

# Beneficios del manejo de excepciones

Gracias a estas validaciones el programa ahora:

- Detecta errores antes de ejecutar cálculos.
- Evita operaciones matemáticas inválidas.
- Hace el código más robusto.
- Mejora la seguridad del programa.
- Facilita el mantenimiento y depuración.

---
