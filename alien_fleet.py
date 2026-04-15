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
        alien_width = self.settings.alien_width
        screen_width = self.settings.screen_width

        fleet_height, fleet_width = self.calculate_fleet_size(alien_height, screen_height, alien_width, screen_width)

        y_offset, x_offset = self.calculate_offsets(alien_height, screen_height, alien_width, fleet_height, fleet_width)

        self._create_rectangle_fleet(alien_height, alien_width, fleet_height, fleet_width, y_offset, x_offset)

    def _create_rectangle_fleet(self, alien_height, alien_width, fleet_height, fleet_width, y_offset, x_offset):
        for col in range(fleet_width):
            current_x = alien_width * col + x_offset
            for row in range(fleet_height):
                current_y = alien_height * row + y_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_height, screen_height, alien_width, fleet_height, fleet_width):
        half_screen = self.settings.screen_width//2
        fleet_vertical_space = fleet_height * alien_height
        fleet_horizontal_space = fleet_width * alien_width
        y_offset = int((screen_height - fleet_vertical_space)//2)
        x_offset = int((half_screen + fleet_horizontal_space)//2)
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_height: int, screen_height: int, alien_width: int, screen_width: int) -> tuple:
        fleet_height = (screen_height//alien_height)
        fleet_width = ((screen_width / 2)//alien_width)

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        return int(fleet_height), int(fleet_width)
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self) -> None:
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._move_alien_fleet()
                self.fleet_direction *= -1
                break

    def _move_alien_fleet(self) -> None:
        for alien in self.fleet:
            alien.x -= self.fleet_movement_speed

    def update_fleet(self) -> None:
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self) -> None:
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_left(self) -> bool:
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False