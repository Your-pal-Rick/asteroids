""" 
Asteroids Game - Game Module

This module contains the main game loop and initialisation logic for the Asteroids.
It handles rendering, game updates, collision detection, and player input. """

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

class Game:
    """ Class Docstring """

    def __init__(self):
        """ Initialise the game """
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()

        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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