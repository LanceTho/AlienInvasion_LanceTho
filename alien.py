"""
alien.py
Lance Thongsavanh
This file has the Alien class
4/15/2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):

    def __init__(self, fleet: "AlienFleet", x: float, y: float) -> None:
        """Initializes variables based on the game

        Args:
            game (AlienInvasion): the current game
            x (float): x-position
            y (float): y-position
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        self.image = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        self.x = self.rect.x
        self.y = self.rect.y

    def update(self) -> None:
        """Moves the alien
        """
        temp_speed = self.settings.fleet_speed

        self.y -= temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Checks if the alien hit the edge of the screen

        Returns:
            bool: returns true if it did, otherwise returns false
        """
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """Displays the alien
        """
        self.screen.blit(self.image, self.rect)