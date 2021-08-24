class Settings:
    """A class to store all Alien Invasion configurations."""

    def __init__(self):
        """Initializes the game configurations."""
        # Screen configurations
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship configurations
        self.ship_speed_factor = 1.5

        # Projectiles configurations
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
