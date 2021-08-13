import sys

import pygame

from settings import Settings


def run_game():
    # Initializes the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Starts the main lace of the game
    while True:

        # Observes keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen on each lace passage
        screen.fill(ai_settings.bg_color)

        # Leaves the most recent screen visible
        pygame.display.flip()


run_game()
