"""
alien_invasion.py
Lance Thongsavanh
This is the main file for the game
4/9/2026
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet

class AlienInvasion:
    """This is the class that creates the game
    """
    
    def __init__(self) -> None:
        """Initializes all of the settings and objects for the game
        """
        
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact = pygame.mixer.Sound(self.settings.impact)
        self.impact.set_volume(0.7)
        
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

    def _check_events(self) -> None:
        """Checks for key presses that the user does
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks for what key is pressed down based on the given event

        Args:
            event (any): key press
        """
        if event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

    def _check_keyup_events(self, event):
        """Checks if the key is not pressed down

        Args:
            event (any): key press
        """
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _update_screen(self):
        """Displays the screen of the game
        """
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        # self.alien.draw_alien()
        self.alien_fleet.draw()
        pygame.display.flip()

    def run_game(self) -> None:
        """Runs the game
        """
        # Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self) -> None:
        # check collisoins for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._reset_level()
            # subtract one life if possible

        # check collisions for aliens and the left side of screen
        if self.alien_fleet.check_fleet_left():
            self._reset_level()

        # check collisions of lasers and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact.play()
            self.impact.fadeout(250)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _reset_level(self) -> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
