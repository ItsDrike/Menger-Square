from contextlib import suppress

import pygame

from src.util import Colors
from src.square import Square
from src.vector import Vector

WIDTH, HEIGHT = 1200, 900
TICK_RATE = 100


class Game:
    def __init__(self, width: int, height: int, fps: int) -> None:
        self.size = self.width, self.height = width, height

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.fps_clock = pygame.time.Clock()
        self.tick_rate = fps

        self.running = True

    def handle_user_event(self) -> None:
        """Handle pygame events (f.e.: quit, click)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    new_squares = []
                    for square in self.squares:
                        new_squares += square.split()
                    self.squares = new_squares
                    print(len(self.squares))

    def redraw_screen(self) -> None:
        """
        Redraw all cells on the screen.

        This does not update the screen, it only redraws it.
        """
        self.screen.fill(Colors.GREY)

        for square in self.squares:
            pygame.draw.rect(self.screen, Colors.WHITE, square.rect)

    def update_screen(self, tick: bool = True) -> None:
        """
        Update the screen accordingly to `redraw_screen`
        also check for user event and tick (if not specified otherwise)
        """

        self.handle_user_event()

        if not self.running:
            return

        self.redraw_screen()
        pygame.display.update()
        if tick:
            self.fps_clock.tick(self.tick_rate)

    def main(self) -> None:
        self.squares = []
        self.squares.append(
            Square(
                Vector(self.width / 2, self.height / 2),
                max(WIDTH, HEIGHT) / 2
            )
        )
        # Main game loop
        while self.running:
            self.update_screen()


game = Game(WIDTH, HEIGHT, TICK_RATE)

with suppress(KeyboardInterrupt):
    game.main()

print("\nStopped")
pygame.quit()
