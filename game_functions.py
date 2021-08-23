import sys

import pygame


def check_keydown_events(event, ship):
    """Responses to keydown."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Responses to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Responses to keyboard and mouse keydown events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Updates the images on the screen and alternate to a new screen."""
    # Redraw the screen on each lace passage
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Leaves the most recent screen visible
    pygame.display.flip()
