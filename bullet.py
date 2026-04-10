"""
bullet.py
Lance Thongsavanh
This file has the Bullet class
4/9/2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """This class handles the ship's shooting

    Args:
        Sprite (_type_): _description_
    """
    
    def __init__(self, game: "AlienInvasion") -> None:
        """Initializes variables based on the game

        Args:
            game (AlienInvasion): the current game
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.image_up = self.image
        self.image_down = pygame.transform.flip(self.image, False, True)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_right = pygame.transform.flip(self.image_left, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = game.ship.rect.center
        self.y = self.rect.y
        self.x = self.rect.x

        self.ship = game.ship

    def update(self) -> None:
        """Moves the position of the bullet by a set speed
        """
        if self.ship.facing == "up":
            self.image = self.image_up
            self.shoot_up()
        elif self.ship.facing == "down":
            self.image = self.image_down
            self.shoot_down()
        elif self.ship.facing == "right":
            self.image = self.image_right
            self.shoot_right()
        elif self.ship.facing == "left":
            self.image = self.image_left
            self.shoot_left()

    def shoot_up(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def shoot_down(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def shoot_right(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def shoot_left(self):
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Displays the bullet
        """
        self.screen.blit(self.image, self.rect)