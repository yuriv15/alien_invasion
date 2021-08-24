import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that administrates projectiles shot by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Creates an object fot the projectile in the ship's actual position."""
        super().__init__()
        self.screen = screen

        # Creates a rectangle for the projectile in (0, 0) and, after that, defines the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Stores the projectile position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the projectile up in the screen."""
        # Updates the decimal position of the projectile
        self.y -= self.speed_factor
        # Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the projectile in the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
