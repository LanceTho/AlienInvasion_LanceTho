"""
settings.py
Lance Thongsavanh
This file houses the settings for the game
4/9/2026
"""

from pathlib import Path
class Settings:
    
    def __init__(self) -> None:
        """Holds all of the set variables for the game
        """
        self.name: str = "Alien Invasion"
        self.screen_width = 1000
        self.screen_height = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_speed = 7
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_speed = 2