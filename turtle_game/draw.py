from turtle import Turtle

from bounding_box import BoundingBox


class TurtleDrawStrategy:

    def __init__(self, color: str, pensize: int) -> None:
        self._color = color
        self._pensize = pensize

    def draw(self, box: BoundingBox) -> None:
        pen = Turtle()
        pen.color(self._color)
        pen.pensize(self._pensize)
        pen.penup()
        pen.setposition(box.bottom_left_corner)
        pen.pendown()

        for _ in range(2):
            pen.forward(box.width)
            pen.left(90)
            pen.forward(box.height)
            pen.left(90)

        pen.hideturtle()
