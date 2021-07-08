import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load the ship image and get it to react
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings
        
        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        """Draw the ship at its current coordinates"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #Update rect object from self.x
        self.rect.x = self.x
        
            
            