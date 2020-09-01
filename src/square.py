import typing as t
from pygame import Rect

from src.vector import Vector


class Square:
    def __init__(self, center: Vector, side: float):
        self.center = center
        self.side = side

    def split(self) -> t.List["Square"]:
        """
        Split the original square into 8 smaller squares
        (Omiting the center one)
        """
        cls = self.__class__
        squares = []
        new_side = self.side / 3
        for i in [new_side, 0, -new_side]:
            for j in [new_side, 0, -new_side]:
                if i == 0 and j == 0:
                    continue
                center = self.center + Vector(i, j)
                squares.append(cls(center, new_side))

        return squares

    @property
    def rect(self) -> Rect:
        vec = Vector(self.side / 2, self.side / 2)
        p2 = self.center - vec
        return Rect(p2.points, (self.side, self.side))
