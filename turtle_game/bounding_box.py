from typing import Protocol


class HasPosition(Protocol):

    def position(self) -> tuple[int, int]:
        ...


class SoundStrategy(Protocol):

    def play(self) -> None:
        ...


class DrawStrategy(Protocol):

    def draw(self, box: "BoundingBox") -> None:
        ...


class BoundingBox:

    def __init__(
        self,
            left_bound: int,
            right_bound: int,
            bottom_bound: int,
            top_bound: int,
            sound_strategy: SoundStrategy,
            draw_strategy: DrawStrategy,
    ) -> None:
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.bottom_bound = bottom_bound
        self.top_bound = top_bound
        self._sound_strategy = sound_strategy
        self._draw_strategy = draw_strategy

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

    def draw(self) -> None:
        self._draw_strategy.draw(self)

    def play_bounce_sound(self):
        self._sound_strategy.play()
