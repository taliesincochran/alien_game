import sys

import pygame

from settings import Settings
from ship import Ship

class AlienGame:
    """ Overall class to manage game assets and state"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print("keydown")
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    print("keyup")
                    self._check_keyup_events(event)
                        
    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
    
    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move the ship[ to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
        
                    
if __name__ == '__main__':
    #Makes a game instance and runs the game
    ai = AlienGame()
    ai.run_game()