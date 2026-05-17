import math

   
# ===================== POINT =====================
# Representa un punto en el plano cartesiano
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x  # Coordenada en X
        self._y = y  # Coordenada en Y

    # -------- GETTERS --------
    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    # -------- SETTERS --------
    def set_x(self, x: float) -> None:
        self._x = x

    def set_y(self, y: float) -> None:
        self._y = y

    # Calcula la distancia entre dos puntos
    def distance_to(self, other: "Point") -> float:
        dx = self._x - other._x  # Diferencia en X
        dy = self._y - other._y  # Diferencia en Y
        return math.sqrt(dx ** 2 + dy ** 2)