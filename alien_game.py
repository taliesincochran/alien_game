import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienGame:
    """ Overall class to manage game assets and state"""
    
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()            
            
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                        
    def _check_keyup_events(self, event):
        """Respond to keyup events"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False 
    
    def _check_keydown_events(self, event):
        """Respond to keydown events"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            self._fire_bullet()
        # Make sure you can exit the game
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet groups"""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
        
    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # For loop to draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        self.bullets.update()
        # Delete bullets when they exit the screeen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))                
        self._update_screen()
    
    def _create_fleet(self):
        """"Create a fleet of alien ships"""
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        self.aliens.add(alien)
            
if __name__ == '__main__':
    #Makes a game instance and runs the game
    ai = AlienGame()
    ai.run_game()