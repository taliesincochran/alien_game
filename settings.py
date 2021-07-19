"""Settings Class"""

class Settings:
    """A class to store all the settings for Alien Invasion Game"""
    def __init__(self):
        """Initialize the game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_limit = 3
        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1
        # fleet direction (1 is right, -1 left)
        self.fleet_direction = 1
        
        