import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initializes the spaceship and define it's original position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads the image of the ship and get it's rect\
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Initializes each new ship in the inferior central area of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Stores a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship position accordingly to the movement flag."""
        # Updates the ship's center value, and not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Updates the rect object accordingly to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship in it's actual position."""
        self.screen.blit(self.image, self.rect)
