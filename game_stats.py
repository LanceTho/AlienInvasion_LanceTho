"""
game_stats.py
Lance Thongsavanh
This file holds the GameStats class
4/22/2026
"""

import json
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
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """initializes the high score if there is a file, if there is not a file then it creates a new file to store the high score
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        else:
            self.high_score = 0
            self.save_scores()

    def save_scores(self) -> None:
        """saves the score in the file
        """
        scores = {
            "high_score": self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self) -> None:
        """resets the stats for the game to the default values
        """
        self.ships_left = self.settings.starting_ship_amount
        self.score = 0
        self.level = 1

    def update(self, colliisions) -> None:
        """updates the score based on the collisions

        Args:
            colliisions (Group): group of collisions
        """
        self._update_score(colliisions)
        self._update_max_score()
        self._update_high_score()

    def _update_score(self, colliisions) -> None:
        """updates the score

        Args:
            colliisions (Group): group of collisions
        """
        for alien in colliisions.values():
            self.score += self.settings.alien_points
    
    def _update_max_score(self) -> None:
        """updates the max score
        """
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_high_score(self) -> None:
        """updates the high score
        """
        if self.score > self.high_score:
            self.high_score = self.score

    def update_level(self) -> None:
        """increases the level by 1
        """
        self.level += 1