import sys

import pygame


class BaseMainloop:
    def __init__(self, screen_size: tuple[int, int]) -> None:
        self._screen_size = screen_size
        self.fullscreen = False

    @property
    def fullscreen(self) -> bool:
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, fullscreen: bool) -> None:
        self._screen = pygame.display.set_mode(
            self._screen_size, pygame.FULLSCREEN if fullscreen else 0
        )
        self._fullscreen = fullscreen

    def before_update(self) -> None:
        self._events = pygame.event.get()

    def update(self) -> None:
        for event in self._events:
            if event.type == pygame.QUIT:
                self.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.fullscreen = not self.fullscreen
        pygame.display.update()

    def after_update(self) -> None:
        pass

    def quit(self) -> None:
        sys.exit()
