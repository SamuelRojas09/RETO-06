from typing import List

from Shape.triangle import Triangle
from Shape.point import Point
       
        
# Triángulo isósceles: al menos dos lados iguales
class Isosceles(Triangle):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        if not (
            abs(a - b) < 1e-6 or
            abs(b - c) < 1e-6 or
            abs(a - c) < 1e-6
        ):
            raise ValueError("Not an isosceles triangle")
