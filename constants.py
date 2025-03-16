"""
Asteroids Game - Constants Module

Contains game configurations in the form of dataclasses. All are nested and accessible
within the GameSettings dataclass.

A GameSettings singleton, settings, is created at the bottom of the module to be imported by game.

Available settings:
    - setings.               ... fps
    - settings.screen.       ... width      height      center
    - settings.color.        ... background outline
    - settings.player.       ... radius     color       thickness   speed       turn_speed
    - settings.player.shot.  ... radius     color       thickness   speed       cooldown
    - settings.asteroid.     ... kinds      spawn_rate  color       thickness   min_radius  max_radius
    - settings.exit_m        ... manual     dead
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
    # Sprite attributes - Sprite radius, outline colo(u)r and thickness
    radius: int = 5
    color: tuple[int, int, int] = (255, 128, 128)
    thickness: int = 0 # Filled

    # Weapon attributes - firing cooldown and shot speed
    speed: int = 650
    cooldown: float = 0.3

@dataclass(frozen=True)
class PlayerConstants:
    """Stores attributes for player movement and sprite size, and contains ShotConstants"""
    # Sprite attributes - sprite radius, outline color and thickness
    radius: int = 20
    color: tuple[int, int, int] = (0, 122, 204)
    thickness: int = 0

    # Movement attributes - fly speed and turn rate
    speed: int = 380
    turn_speed: int = 360

    # Nested ShotConstants
    shot: ShotConstants = ShotConstants()

@dataclass(frozen=True)
class AsteroidConstants:
    """Stores attrtibutes for asteroid spawn rate, size, and size diversity"""
    # Number of asteroid sizes
    kinds: int = 4

    # Spawn rate (s) of asteroids
    spawn_rate: float = 1

    # Sprite outline color and thickness
    color: tuple[int, int, int] = (192, 192, 192)
    thickness: int = 0

    # Minimum radius of asteroid sprite
    min_radius: int = 20

    # Maximum radius of asteroid sprite, given as min_radius * kinds (of asteroid)
    @property
    def max_radius(self) -> int:
        return self.min_radius * self.kinds

@dataclass(frozen=True)
class ExitMessages:
    """Contains strings for game exit messages printed to the terminal"""
    # Exit message for manual game close
    manual = "Game closed manually. Thanks for playing!"
    # Exit message for running out of health (currently one asteroid collision)
    dead = "Game closed due to critical ship damage. Thanks for playing!"

@dataclass(frozen=True)
class GameSettings:
    """Stores game updates per second and nested dataclasses:
        SCREEN, COLOR, PLAYER, ASTEROID"""

    # settings.screen.       ... width height center
    screen: ScreenSettings = ScreenSettings()
    
    # settings.color.        ... background outline
    color: ColorSettings = ColorSettings()

    # settings.player.       ... radius color thickness speed turn_speed
    # settings.player.shot.    ... radius color thickness speed cooldown
    player: PlayerConstants = PlayerConstants()

    # settings.asteroid.     ... kinds spawn_rate color thickness min_radius max_radius
    asteroid: AsteroidConstants = AsteroidConstants()

    # settings.exit_m        ... manual dead
    exit_m: ExitMessages = ExitMessages()

    # Updates and renders per second
    fps: int = 60

# Singleton to be imported by other modules
settings = GameSettings()