"""
game_stats.py
Lance Thongsavanh
This file holds the GameStats class
4/15/2026
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """This class handles the overall stats for the game
    """

    def __init__(self, game: "AlienInvasion") -> None:
        """Initializes the variables based on the game

        Args:
            game (AlienInvasion): the current game
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_amount
        self.score = 0
        self.level = 1

    def update(self, colliisions) -> None:
        # update score
        self._update_score(colliisions)

        # update max_score
        self._update_max_score()
    
        # update high_score


    def _update_score(self, colliisions):
        for alien in colliisions.values():
            self.score += self.settings.alien_points
        #print(f"Basic: {self.score}")
    
    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Max: {self.max_score}")

    def update_level(self) -> None:
        self.level += 1
        #print(self.level)