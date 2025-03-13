"""
Asteroids Game - Main Module

This module contains the main game loop and initialisation logic for the Asteroids.
It handles rendering, game updates, collision detection, and player input.

Usage:
    Run this file directly to start the game:
    $ python main.py
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Local application imports
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def initialise_game():
    """Set up game environment"""
    pygame.init()


def main():
    initialise_game()
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_player = Player(PLAYER_SPAWN_POSITION[0], PLAYER_SPAWN_POSITION[1])
    my_asteroidfield = AsteroidField()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(my_player):
                sys.exit("Game over!")

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(BLACK)

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FRAMES_PER_SECOND) / 1000 # to milliseconds

if __name__ == "__main__":
    main()
