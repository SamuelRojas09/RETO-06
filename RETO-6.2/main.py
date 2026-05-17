import math

from Shape.point import Point
from Shape.line import Line
from Shape.shape import Shape
from Shape.triangle import Triangle
from Shape.rectangle import Rectangle
from Shape.square import Square
from Shape.scalene import Scalene
from Shape.isosceles import Isosceles
from Shape.right_triangle import RightTriangle
from Shape.equilateral import Equilateral
  

# ===================== MAIN =====================
if __name__ == "__main__":

    # Función para mostrar información de cualquier figura
    def show_shape(name: str, shape: Shape) -> None:
        print(f"\n--- {name} ---")

        area = shape.compute_area()
        perimeter = shape.compute_perimeter()
        angles = [round(a, 2) for a in shape.inner_angles()]

        print(f"Area        : {area:.2f}")
        print(f"Perimeter   : {perimeter:.2f}")
        print(f"Angles (°)  : {angles}")
        print(f"Is regular  : {shape.is_regular()}")

    print("\n==============================")
    print("     GEOMETRY TEST PROGRAM")
    print("==============================")

    # Prueba de Point y Line
    print("\n=== POINT & LINE ===")
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    line = Line(p1, p2)

    print(f"Distance between points : {p1.distance_to(p2):.2f}")
    print(f"Line length             : {line.length():.2f}")

    # Prueba de triángulo general
    triangle = Triangle([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("General Triangle", triangle)

    # Prueba de rectángulo
    rectangle = Rectangle([
        Point(0, 0), Point(4, 0), Point(4, 2), Point(0, 2)
    ])
    show_shape("Rectangle", rectangle)

    # Prueba de cuadrado
    square = Square([
        Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)
    ])
    show_shape("Square", square)

    print("\n=== SPECIAL TRIANGLES ===")

    # Prueba de triángulos especiales
    scalene = Scalene([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("Scalene Triangle", scalene)

    isosceles = Isosceles([Point(0, 0), Point(4, 0), Point(2, 3)])
    show_shape("Isosceles Triangle", isosceles)

    right = RightTriangle([Point(0, 0), Point(4, 0), Point(4, 3)])
    show_shape("Right Triangle", right)

    equilateral = Equilateral([
        Point(0, 0), Point(2, math.sqrt(12)), Point(4, 0)
    ])
    show_shape("Equilateral Triangle", equilateral)

    print("\n==============================")
    print("        END OF TEST")
    print("==============================")
