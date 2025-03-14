""" 
Asteroids Game - Game Module

This module contains the Game class, which is responsible for initialising the game
and running the game loop.

On initialisation it declares Game class variables, assigns classes to groups, and
creates game instances.

In the run() loop it handles event checks, game object updates, collision checks, 
player inputs, and rendering.

A Game singleton is created at the end of this module to be imported by main.
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Local application imports
from constants import settings # type: GameSettings
from player import Player, Shot
from asteroid import Asteroid, AsteroidField

class Game:
    """ Game class - Initialises game and handles game loop"""
    def __init__(self):
        """Runs on game start"""
        self._init_game()

    def _init_game(self):
        """Initialise game state, groups, objects"""
        self._init_game_state()
        self._init_pygame()
        self._create_sprite_groups()
        self._assign_containers()
        self._create_game_objects()

    def _init_game_state(self):
        """Initialise game state variables"""
        self.dt = 0
        self.running = True
        self.exit_message = "Game closed. Thanks for playing!"

    def _init_pygame(self):
        """Initialise pygame, create game clock and screen"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
        pygame.display.set_caption("Asteroids - But this time, it's Blue")

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
        self.my_player = Player(settings.screen.center[0], settings.screen.center[1])
        self.my_asteroidfield = AsteroidField()

    def handle_events(self):
        """Check events for quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def handle_collisions(self):
        """Handle collisions between game objects"""
        # Player-Asteroid collision check
        for asteroid in self.asteroids:
            if asteroid.is_colliding(self.my_player):
                sys.exit("Hit by an asteroid. " + self.exit_message)

        # Shot-Asteroid collision check
        for asteroid in self.asteroids:
            for shot in self.shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()

    def update(self):
        """Update state of updatable-grouped objects"""
        self.updatable.update(self.dt)

    def render(self):
        """Render the game"""
        # First fill screen with defined background color
        self.screen.fill(settings.color.background)
        # Draw all drawable-grouped objects
        for member in self.drawable:
            member.draw(self.screen)
        # Update display
        pygame.display.flip()

    def _update_dt(self):
        """Set dt to time since last frame and regulate frame rate"""
        self.dt = self.clock.tick(settings.fps) / 1000 # to seconds

    def run(self):
        """Main game loop. Runs Game methods to check for quit attempts,
        update game objects, check for object collisions, render the
        background and game objects, and regulate frame/update rate (dt)."""
        while self.running:
            self.handle_events()
            self.update()
            self.handle_collisions()
            self.render()
            self._update_dt()

# Singleton of class Game to be imported into main.py
game = Game()