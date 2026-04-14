"""
ship.py
Lance Thongsavanh
This file has the Ship class
4/9/2026
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship():
    """This class handles the ship that the player controls
    """
    
    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal") -> None:
        """Initializes variables based on the game and arsenal

        Args:
            game (AlienInvasion): The current game
            arsenal (Arsenal): The ship's loadout
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.image = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft

        self.moving_down = False
        self.moving_up = False
        self.y = self.rect.y
        self.arsenal = arsenal

    def update(self) -> None:
        """Updates the ship's position
        """
        # updating position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Moves the ship up or down if it's still within the boundaries of the screen
        """
        temp_speed = self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed

        self.rect.y = self.y

    def draw(self) -> None:
        """Draws the ship
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Calls the fire_bullet function from the Arsenal class

        Returns:
            bool: True if it did fire and False if it didn't
        """
        return self.arsenal.fire_bullet()