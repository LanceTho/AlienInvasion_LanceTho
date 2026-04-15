"""
alien_fleet.py
Lance Thongsavanh
This file has the AlienFleet class
4/15/2026
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_movement_speed = self.settings.fleet_movement_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        alien_height = self.settings.alien_height
        screen_height = self.settings.screen_height

        fleet_height = self.calculate_fleet_size(alien_height, screen_height)

        # half_screen = self.settings.screen_width
        fleet_vertical_space = fleet_height * alien_height
        y_offset = int((screen_height - fleet_vertical_space)//2)

        for row in range(fleet_height):
            current_y = alien_height * row + y_offset
            self._create_alien(self.settings.screen_width - 40, current_y)

    def calculate_fleet_size(self, alien_height: int, screen_height: int) -> int:
        fleet_height = (screen_height//alien_height)

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return fleet_height
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self) -> None:
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()