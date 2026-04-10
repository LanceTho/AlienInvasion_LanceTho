"""
arsenal.py
Lance Thongsavanh
This file has the Arsenal class
4/9/2026
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """This class handles the weapons for the ship
    """

    def __init__(self, game: "AlienInvasion") -> None:
        """Initializes variables based on the game

        Args:
            game (AlienInvasion): the current game
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Updates the screen
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Checks if the bullet is off screen and deletes if it is
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.top >= self.settings.screen_height or bullet.rect.left <= 0 or bullet.rect.right >= self.settings.screen_width:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the bullet
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """The ship fires if there are less than the amount on screen

        Returns:
            bool: returns True if it does fire and False if it doesn't
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False

    