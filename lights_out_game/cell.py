import random
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Optional

from .light import Light


@dataclass(frozen=True)
class Cell:
    x: int
    y: int
    light: Light


class Cells(Iterable[Cell]):
    def __init__(self, size: int) -> None:
        self._size = size
        self._cells = [
            [Cell(x, y, Light.OFF) for x in range(size)] for y in range(size)
        ]

    def __iter__(self) -> Iterator[Cell]:
        for x in range(self._size):
            for y in range(self._size):
                cell = self._get_cell(x, y)
                if cell:
                    yield cell

    @property
    def all_lights_are_off(self) -> bool:
        return all(cell.light.is_off for cell in self)

    def push(self, x: int, y: int) -> None:
        self._toggle_light(x - 1, y)
        self._toggle_light(x, y - 1)
        self._toggle_light(x, y)
        self._toggle_light(x + 1, y)
        self._toggle_light(x, y + 1)

    def randomize(self) -> int:
        push_count = 0
        for x in range(self._size):
            for y in range(self._size):
                if random.randint(0, 1):
                    self.push(x, y)
                    push_count += 1
        if self.all_lights_are_off:
            return self.randomize()
        else:
            return push_count

    def _set_cell(self, x: int, y: int, cell: Cell) -> None:
        if 0 <= x < self._size and 0 <= y < self._size:
            self._cells[y][x] = cell

    def _get_cell(self, x: int, y: int) -> Optional[Cell]:
        if 0 <= x < self._size and 0 <= y < self._size:
            return self._cells[y][x]
        else:
            return None

    def _set_light(self, x: int, y: int, light: Light) -> None:
        self._set_cell(x, y, Cell(x, y, light))

    def _toggle_light(self, x: int, y: int) -> None:
        cell = self._get_cell(x, y)
        if cell:
            self._set_light(x, y, cell.light.toggled)
