import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initializes the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Creates a ship
    ship = Ship(screen)

    # Starts the main lace of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
