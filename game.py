""" 
Asteroids Game - Game Module

This module contains the main game loop and initialisation logic for the Asteroids.
It handles rendering, game updates, collision detection, and player input.
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Local application imports
from constants import *
from player import Player, Shot
from asteroid import Asteroid, AsteroidField

class Game:
    """ Game class - Initialises game and handles
    entirety of game loop. Will soon be neater. """
    def __init__(self):
        self._init_game()

    def _init_game(self):
        """Initialise the game"""
        self._init_game_state()
        self._init_pygame()
        self._create_sprite_groups()
        self._assign_containers()
        self._create_game_objects()

    def _init_game_state(self):
        """Initialise game state variables (only a small timer for shoot cooldown right now)"""
        self.dt = 0

    def _init_pygame(self):
        """Initialise pygame, create game clock and screen"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids - Your pal, Rick")

    def _create_sprite_groups(self):
        """Create sprite groups for game entities, for easy iteration"""
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()

    def _assign_containers(self):
        """Assign sprite classes to groups"""
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

    def _create_game_objects(self):
        """Create player ship and asteroid field instances"""
        self.my_player = Player(PLAYER_SPAWN_POSITION[0], PLAYER_SPAWN_POSITION[1])
        self.my_asteroidfield = AsteroidField()

    def run(self):
        """ Temporarily transferring unrefactored main loop in here """
        
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            self.updatable.update(self.dt)

            for asteroid in self.asteroids:
                if asteroid.is_colliding(self.my_player):
                    sys.exit("Game over!")

            for asteroid in self.asteroids:
                for shot in self.shots:
                    if asteroid.is_colliding(shot):
                        shot.kill()
                        asteroid.split()

            self.screen.fill(BLACK)

            for member in self.drawable:
                member.draw(self.screen)

            pygame.display.flip()

            self.dt = self.clock.tick(FRAMES_PER_SECOND) / 1000 # to milliseconds