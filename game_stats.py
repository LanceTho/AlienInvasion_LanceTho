"""
game_stats.py
Lance Thongsavanh
This file holds the GameStats class
4/15/2026
"""

class GameStats():
    """This class handles the amount of ships left
    """

    def __init__(self, ship_limit: int) -> None:
        """Initializes the number of ships left

        Args:
            ship_limit (int): the player's lives
        """
        self.ships_left = ship_limit