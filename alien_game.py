import sys

import pygame

class AlienGame:
    """ Overall class to manage game assets and state"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        # Sets the background color
        self.bg_color = (230,230,230)
    
    def run_game(self):
        """Start the main game loop"""
        while True:
            # Set keyboard and mouse listeners
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                # Redraw screen with each pass of the loop
                self.screen.fell(self.bg_color)
                # Make most recently drawn screen visible
                pygame.display.flip()
                    
if __name__ == '__main__':
    #Makes a game instance and runs the game
    ai = AlienGame()
    ai.run_game()