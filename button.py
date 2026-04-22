"""
button.py
Lance Thongsavanh
This has the Button Class
4/22/2026
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """This class handles the start button for the user to click
    """

    def __init__(self, game: "AlienInvasion", msg: str) -> None:
        """Initializes variables based on the game and message

        Args:
            game (AlienInvasion): the current game
            msg (str): message that shows on the button
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)
        
    def _prep_msg(self, msg: str) -> None:
        """creates a rectangle for the message

        Args:
            msg (str): the text for the button
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """draws the button and the text
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos: tuple) -> bool:
        """checks if the button is clicked by the mouse

        Args:
            mouse_pos (tuple): the x-position and y-position of the mouse

        Returns:
            bool: returns true if the mouse clicked it, otherwise returns false
        """
        return self.rect.collidepoint(mouse_pos)