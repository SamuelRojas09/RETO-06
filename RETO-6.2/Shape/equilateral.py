from typing import List

from Shape.point import Point
from Shape.triangle import Triangle


# ===================== EQUILATERAL =====================
# Triángulo equilátero
class Equilateral(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        # Verifica que todos los lados sean iguales
        if not self.is_regular():
            raise ValueError(
                "Not an equilateral triangle."
            )

    def is_regular(self) -> bool:
        return True