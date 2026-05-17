from typing import List

from Shape.rectangle import Rectangle
from Shape.point import Point

    
# ===================== SQUARE =====================
# Representa un cuadrado (hereda de Rectangle)
class Square(Rectangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Se verifica que todos los lados tengan la misma longitud
        sides = [edge.length() for edge in self._edges]
        first = sides[0]

        for side in sides:
            if abs(side - first) > 1e-6:  # Tolerancia por errores decimales
                raise ValueError("Not a square")

    # Un cuadrado sí es una figura regular
    def is_regular(self) -> bool:
        return True
