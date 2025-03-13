"""
Asteroids Game - Main Module

Based on the boot.dev (https://boot.dev) project, Build Asteroids Using Python,
which I am refactoring as practise with OOP principles in mind.

This is the entry point, which initialises and runs the game using the Game class.

Usage:
    Run this file directly to start the game:
    $ python main.py

Dependencies:
    - Pygame (https://pygame.org)
    - Python 3.x

Controls:
    - WASD:         Move ship
    - Space bar:    Fire
    - ESC:          Quit game (not implemented yet)
"""

# Local application imports
from game import Game

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
