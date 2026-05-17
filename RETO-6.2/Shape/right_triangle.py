from typing import List

from Shape.triangle import Triangle
from Shape.point import Point

       
# Triángulo rectángulo: cumple el teorema de Pitágoras
class RightTriangle(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        sides = sorted([self.get_a(), self.get_b(), self.get_c()])

        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) > 1e-6:
            raise ValueError("Not a right triangle")
