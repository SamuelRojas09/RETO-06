from typing import List

from Shape.point import Point
from Shape.line import Line
    
          
# ===================== SHAPE =====================
# Clase base para todas las figuras geométricas
class Shape:
    def __init__(self, vertices: List[Point]) -> None:
        self._vertices = vertices      # Lista de vértices compuesta por objetos Point
        self._edges: List[Line] = []   # Lista de lados compuesta por objetos Line

    # -------- GETTERS --------
    def get_vertices(self) -> List[Point]:
        return self._vertices

    def get_edges(self) -> List[Line]:
        return self._edges

    # -------- SETTERS --------
    def set_vertices(self, vertices: List[Point]) -> None:
        self._vertices = vertices

    def set_edges(self, edges: List[Line]) -> None:
        self._edges = edges

    # Calcula el perímetro sumando la longitud de todos los lados
    def compute_perimeter(self) -> float:
        return sum(edge.length() for edge in self._edges)

    # Obliga a las subclases a implementarlo
    def compute_area(self) -> float:
        raise NotImplementedError

    # Calcula los ángulos internos
    def inner_angles(self) -> List[float]:
        raise NotImplementedError

    # Indica si la figura es regular (por defecto False)
    def is_regular(self) -> bool:
        return False
