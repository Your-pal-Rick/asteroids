"""
Asteroids Game - Circleshape Module

Contains the CircleShape class, which inherits attributes from pygame.sprite.Sprite
and acts as parent class to Player, Shot, and Asteroid.
Passes down position, velocity, and radius variables and is_colliding(), draw(),
and update() methods.
"""

# Third-party imports
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Check for container group
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Set position based on passed x, y ints
        self.position = pygame.Vector2(x, y)
        
        # Set velocity to (0,0) vector to start
        self.velocity = pygame.Vector2(0, 0)
        
        # Set radius based on passed radius int
        self.radius = radius

    def is_colliding(self, other):
        """Check if distance between center position of two CircleShape objects is less than their radiuses combined"""
        if pygame.Vector2.distance_to(self.position, other.position) <= self.radius + other.radius:
            return True
        return False

    def draw(self, screen):
        # Child classes will override
        pass

    def update(self, dt):
        # Child classes will override
        pass