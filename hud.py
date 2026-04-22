"""
hud.py
Lance Thongsavanh
This has the HUD Class
4/22/2026
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    """This class handles the display for the scores and lives
    """

    def __init__(self, game: "AlienInvasion") -> None:
        """Initializes variables based on the game

        Args:
            game (AlienInvasion): the current game
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self) -> None:
        """sets up the image used to represent lives
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (self.settings.ship_width, self.settings.ship_height))
        self.life_image = pygame.transform.rotate(self.life_image, 270)
        self.life_rect = self.life_image.get_rect()

    def update_scores(self) -> None:
        """updates all of the scores
        """
        self._update_max_score()
        self._update_score()
        self._update_high_score()

    def _update_score(self) -> None:
        """updates the score
        """
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding
    
    def _update_max_score(self) -> None:
        """updates the max score
        """
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_high_score(self) -> None:
        """updates the high score
        """
        high_score_str = f"High-Score: {self.game_stats.high_score: ,.0f}"
        self.high_score_image = self.font.render(high_score_str, True, self.settings.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def update_level(self) -> None:
        """updates the level
        """
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.padding

    def _draw_lives(self) -> None:
        """draws the lives remaining
        """
        current_x = self.settings.screen_width - self.padding * 3
        current_y = self.settings.screen_height - self.padding * 3
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x -= self.life_rect.width + self.padding

    def draw(self) -> None:
        """draws the HUD
        """
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()