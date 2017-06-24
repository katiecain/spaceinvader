class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4

        # Alien settings
        self.alien_space = 1.5
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right and -1 is left
        self.fleet_direction = 1
