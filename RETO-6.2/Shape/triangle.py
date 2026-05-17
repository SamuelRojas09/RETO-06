import math
from typing import List

from Shape.point import Point
from Shape.line import Line
from Shape.shape import Shape


# ===================== TRIANGLE =====================
# Representa un triángulo general
class Triangle(Shape):

    def __init__(self, vertices: List[Point]) -> None:

        # Verifica que el triángulo tenga
        # exactamente 3 vértices
        if len(vertices) != 3:
            raise ValueError(
                "A triangle must have exactly 3 vertices."
            )

        super().__init__(vertices)

        # Se crean los 3 lados del triángulo
        self._edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0]),
        ]

        # Verifica que los puntos no estén alineados
        # Si el área es 0, no existe un triángulo válido
        if self.compute_area() == 0:
            raise ValueError(
                "The vertices do not form a valid triangle."
            )

    # Métodos para obtener las longitudes de los lados
    def get_a(self) -> float:
        return self._edges[0].length()

    def get_b(self) -> float:
        return self._edges[1].length()

    def get_c(self) -> float:
        return self._edges[2].length()

    # Área usando la fórmula de Herón
    def compute_area(self) -> float:

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        s = (a + b + c) / 2

        return math.sqrt(
            s * (s - a) * (s - b) * (s - c)
        )

    # Calcula los ángulos internos
    def inner_angles(self) -> List[float]:

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        angle_A = math.degrees(
            math.acos(
                (b**2 + c**2 - a**2)
                / (2 * b * c)
            )
        )

        angle_B = math.degrees(
            math.acos(
                (a**2 + c**2 - b**2)
                / (2 * a * c)
            )
        )

        angle_C = 180.0 - angle_A - angle_B

        return [angle_A, angle_B, angle_C]

    # Un triángulo es regular si todos sus lados son iguales
    def is_regular(self) -> bool:

        a = self.get_a()
        b = self.get_b()
        c = self.get_c()

        return (
            abs(a - b) < 1e-6
            and abs(b - c) < 1e-6
        )