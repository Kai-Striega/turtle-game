from dataclasses import dataclass
from typing import Protocol


class HasPosition(Protocol):

    def position(self) -> tuple[int, int]:
        ...


class SoundStrategy(Protocol):

    def play(self) -> None:
        ...


class DrawBoundingBoxStrategy(Protocol):

    def draw(self, box: "BoundingBox") -> None:
        ...


@dataclass
class Bounds:
    left: int
    right: int
    bottom: int
    top: int


class BoundingBox:

    def __init__(self, bounds: Bounds, sound_strategy: SoundStrategy, draw_strategy: DrawBoundingBoxStrategy) -> None:
        self._bounds = bounds
        self._sound_strategy = sound_strategy
        self._draw_strategy = draw_strategy

    def __contains__(self, item: HasPosition) -> bool:
        x, y = item.position()
        return self._is_in_x_bound(x) and self._is_in_y_bound(y)

    @property
    def width(self) -> int:
        return abs(self._bounds.left) + abs(self._bounds.right)

    @property
    def height(self) -> int:
        return abs(self._bounds.bottom) + abs(self._bounds.top)

    @property
    def bottom_left_corner(self) -> tuple[int, int]:
        return self._bounds.left, self._bounds.bottom

    def _is_in_x_bound(self, x: int | float) -> bool:
        return self._bounds.left < x < self._bounds.right

    def _is_in_y_bound(self, y: int | float) -> bool:
        return self._bounds.bottom < y < self._bounds.top

    def draw(self) -> None:
        self._draw_strategy.draw(self)

    def play_bounce_sound(self):
        self._sound_strategy.play()
