"""
Asteroids Game - Main Module

Program is based on the boot.dev (https://boot.dev) project, Build Asteroids Using Python,
which I refactored as a learning exercise. The game state and its objects are initialised
in the Game class (game.py).

The Player, Shot, Asteroid, and Asteroidfield classes from their respective *.py files
define the settings and behaviours of their instances. The CircleShape class servers as a
parent class to the object classes just mentioned. The GameSettings dataclass stores all
needed constants and values using nesting. This makes it easy to add modules in future.

This is the entry point, which imports an initialised Game type object and then runs its
main loop.

Usage:
    Run this file directly to start the game:
    $ python main.py

Dependencies:
    - Pygame (https://pygame.org)
    - Python 3.x

Controls:
    - WASD:         Move ship
    - Space bar:    Fire
    - ESC:          Quit game
"""

# Local application imports
from game import game # type: Game

def main():
    """Run infinite game loop until quit initiated"""
    game.run()

if __name__ == "__main__":
    """Failsafe to ensure program isn't run when imported"""
    main()
