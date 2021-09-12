from enum import Enum, auto

import pygame

from .base_mainloop import BaseMainloop
from .cell import Cells
from .color import Color


class Scene(Enum):
    PLAYING = auto()
    CLEARED = auto()


class Mainloop(BaseMainloop):
    def __init__(self) -> None:
        self._cell_size = 100
        self._cells = Cells(size=5)
        self._reset_game()
        self._font = pygame.font.Font(None, 60)
        super().__init__(screen_size=(500, 500))

    def _reset_game(self) -> None:
        self._push_count = 0
        self._minimum_required_push_count = self._cells.randomize()
        self._scene = Scene.PLAYING

    def _check_if_cleared(self) -> None:
        if self._cells.all_lights_are_off:
            self._scene = Scene.CLEARED

    def _handle_mouse_click(self) -> None:
        if any(event.type == pygame.MOUSEBUTTONDOWN for event in self._events):
            x, y = pygame.mouse.get_pos()
            cell_x = x // self._cell_size
            cell_y = y // self._cell_size
            self._cells.push(cell_x, cell_y)
            self._push_count += 1

    def _draw_cells(self) -> None:
        for cell in self._cells:
            color = Color.LIGHT_ON if cell.light.is_on else Color.LIGHT_OFF
            rect = [
                cell.x * self._cell_size,
                cell.y * self._cell_size,
                self._cell_size,
                self._cell_size,
            ]
            pygame.draw.rect(self._screen, color, rect)

    def _draw_clear_scene(self) -> None:
        score = 100 - (self._push_count - self._minimum_required_push_count)
        self._screen.blit(
            self._font.render("CONGRATULATIONS!", True, Color.TEXT), [10, 100]
        )
        self._screen.blit(
            self._font.render(f"Score: {score} / 100", True, Color.TEXT), [10, 200]
        )
        self._screen.blit(
            self._font.render("Press Space to restart", True, Color.TEXT), [10, 300]
        )

    def _check_restart(self) -> None:
        if any(
            event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
            for event in self._events
        ):
            self._minimum_required_push_count = self._cells.randomize()
            self._reset_game()

    def update(self) -> None:
        if self._scene == Scene.PLAYING:
            self._screen.fill(Color.BACKGROUND)
            self._check_if_cleared()
            self._handle_mouse_click()
            self._draw_cells()
        elif self._scene == Scene.CLEARED:
            self._draw_clear_scene()
            self._check_restart()
        super().update()
