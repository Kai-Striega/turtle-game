from turtle import Turtle
from typing import Protocol


class HasPosition(Protocol):

    def position(self) -> tuple[int, int]:
        ...


class BoundingBox:

    def __init__(self, left_bound: int, right_bound: int, bottom_bound: int, top_bound: int) -> None:
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.bottom_bound = bottom_bound
        self.top_bound = top_bound

    def __contains__(self, item: HasPosition) -> bool:
        x, y = item.position()
        return self._is_in_x_bound(x) and self._is_in_y_bound(y)

    @property
    def width(self) -> int:
        return abs(self.left_bound) + abs(self.right_bound)

    @property
    def height(self) -> int:
        return abs(self.bottom_bound) + abs(self.top_bound)

    def _is_in_x_bound(self, x: int | float) -> bool:
        return self.left_bound < x < self.right_bound

    def _is_in_y_bound(self, y: int | float) -> bool:
        return self.bottom_bound < y < self.top_bound

    def draw(self, color: str, pensize: int) -> None:
        pen = Turtle()
        pen.color(color)
        pen.pensize(pensize)
        pen.penup()
        pen.setposition(self.left_bound, self.bottom_bound)
        pen.pendown()

        for _ in range(2):
            pen.forward(self.width)
            pen.left(90)
            pen.forward(self.height)
            pen.left(90)

        pen.hideturtle()

