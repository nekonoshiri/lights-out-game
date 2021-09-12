import pygame

from .mainloop import Mainloop


def main() -> None:
    fps = 60
    pygame.init()
    try:
        mainloop = Mainloop()
        clock = pygame.time.Clock()
        while True:
            mainloop.before_update()
            mainloop.update()
            mainloop.after_update()
            clock.tick(fps)
    finally:
        pygame.quit()
