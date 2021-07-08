import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        """Initialize the alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the image of the alien ship and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get.rect()
        
        # Start each ne alien ship at near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien ship's exact horizontal position
        self.x = float(self.rect.x)