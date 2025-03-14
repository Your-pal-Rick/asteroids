"""
Asteroids Game - Constants Module

Contains game configurations in the form of dataclasses.
All are nested within the GameSettings dataclass.
settings = GameSettings singleton (sole instance) is all that has to be imported.
"""

# Standard library imports
from dataclasses import dataclass

@dataclass(frozen=True)
class ScreenSettings:
    """Stores screen dimensions and screen center"""
    # Screen dimensions
    width: int = 1280
    height: int = 720

    # Screen center, for player spawn
    @property
    def center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)

@dataclass(frozen=True)
class ColorSettings:
    """Stores draw colors as tuples: (R,G,B) for background and object outlines"""
    # Background and object outline Colors
    background: tuple[int, int, int] = (1, 8, 77)
    outline: tuple[int, int, int] = (255,255,255)

@dataclass(frozen=True)
class ShotConstants:
    """Stores attributes for player weapon shots"""
    # Weapon attributes - firing cooldown, shot speed and radius
    radius: int = 5
    speed: int = 500
    cooldown: float = 0.3

@dataclass(frozen=True)
class PlayerConstants:
    """Stores attributes for player movement and sprite size, and contains ShotConstants"""
    # Sprite attributes - sprite radius, outline color and thickness
    radius: int = 20
    color: tuple[int, int, int] = (255, 255, 255)
    thickness: int = 2

    # Movement attributes - fly speed and turn rate
    speed: int = 200
    turn_speed: int = 300

    # Nested ShotConstants
    shot: ShotConstants = ShotConstants()

@dataclass(frozen=True)
class AsteroidConstants:
    """Stores attrtibutes for asteroid spawn rate, size, and size diversity"""
    # Number of asteroid sizes
    kinds: int = 3

    # Spawn rate (s) of asteroids
    spawn_rate: float = 0.8

    # Sprite outline color and thickness
    color: tuple[int, int, int] = (255, 255, 255)
    thickness: int = 2

    # Minimum radius of asteroid sprite
    min_radius: int = 20

    # Maximum radius of asteroid sprite, given as min_radius * kinds (of asteroid)
    @property
    def max_radius(self) -> int:
        return self.min_radius * self.kinds

@dataclass(frozen=True)
class GameSettings:
    """Stores game updates per second and nested dataclasses:
        SCREEN, COLOR, PLAYER, ASTEROID"""

    # Usage: settings.screen.       ... width height center
    screen: ScreenSettings = ScreenSettings()
    
    # Usage: settings.color.        ... background outline
    color: ColorSettings = ColorSettings()

    # Usage: settings.player.       ... radius speed turn_speed
    # And: settings.player.shot.    ... radius speed cooldown
    player: PlayerConstants = PlayerConstants()

    # Usage: settings.asteroid.     ... kinds spawn_rate min/max_radius
    asteroid: AsteroidConstants = AsteroidConstants()

    # Updates and renders per second
    fps: int = 60

# Singleton to be imported by other modules
settings = GameSettings()