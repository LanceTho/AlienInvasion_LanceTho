from pathlib import Path
class Settings:
    
    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_width = 1000
        self.screen_height = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"