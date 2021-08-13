import pygame

class Ship:

    def __init__(self, screen):
        """Initializes the spaceship and define it's original position."""
        self.screen = screen

        # Loads the image of the ship and get it's rect\
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Initializes each new ship in the inferior central area of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship in it's actual position."""
        self.screen.blit(self.image, self.rect)
