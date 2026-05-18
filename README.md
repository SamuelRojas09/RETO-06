# Reto 6.2 - Manejo de Excepciones en el paquete Shape

## Descripción

En este reto se agregaron excepciones al paquete `Shape` para mejorar la validación de datos y evitar errores matemáticos o geométricos durante la ejecución del programa.

Las excepciones fueron implementadas siguiendo:

- Reglas de estilo **PEP 8**.
- Uso de **tipado estático** con `typing`.
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

Además, los tres puntos no pueden estar alineados, porque eso no forma un triángulo válido y puede generar errores matemáticos en:

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

### Validación de puntos colineales

```python
area_test = (
    vertices[0].get_x() * (
        vertices[1].get_y() - vertices[2].get_y()
    )
    + vertices[1].get_x() * (
        vertices[2].get_y() - vertices[0].get_y()
    )
    + vertices[2].get_x() * (
        vertices[0].get_y() - vertices[1].get_y()
    )
)

if abs(area_test) < 1e-6:
    raise ValueError(
        "Triangle vertices cannot be collinear."
    )
```

### ¿Qué evita?

- Triángulos inválidos.
- Errores en raíces cuadradas negativas.
- Errores en `math.acos()`.

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

# Beneficios del manejo de excepciones

Gracias a estas validaciones el programa ahora:

- Detecta errores antes de ejecutar cálculos.
- Evita operaciones matemáticas inválidas.
- Hace el código más robusto.
- Mejora la seguridad del programa.
- Facilita el mantenimiento y depuración.

---
