"""
settings.py
Lance Thongsavanh
This file houses the settings for the game
4/15/2026
"""

from pathlib import Path
class Settings:
    
    def __init__(self) -> None:
        """Holds all of the set variables for the game
        """
        self.name: str = "Alien Invasion"
        self.screen_width = 1000
        self.screen_height = 700
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / "Assets" / "file" / "scores.json"

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_width = 40
        self.ship_height = 60

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact = Path.cwd() / "Assets" / "sound" / "impactSound.mp3"

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_direction = 1

        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / "Assets" / "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"
        
    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 5
        self.starting_ship_amount = 3
        
        self.bullet_speed = 7
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_amount = 5

        self.fleet_speed = 2.5
        self.fleet_movement_speed = 40
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale