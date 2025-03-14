"""
Asteroids Game - Player module

And an explanation of it too.
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Local application imports
from constants import settings # type: GameSettings
from circleshape import CircleShape

class Player(CircleShape):
    """AAA"""
    def __init__(self, x, y):
        """AAA"""
        super().__init__(x, y, settings.player.radius)
        self.rotation = 0
        self.cooldown_timer = 0

    def triangle(self):
        """AAA"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        """AAA"""
        pygame.draw.polygon(screen, (settings.player.color), self.triangle(), settings.player.thickness)

    def rotate(self, dt):
        """AAA"""
        self.rotation += settings.player.turn_speed * dt

    def move(self, dt):
        """AAA"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * settings.player.speed * dt

    def shoot(self):
        """AAA"""
        if self.cooldown_timer <= 0:
            shot = Shot(self.position[0], self.position[1], settings.player.shot.radius)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * settings.player.shot.speed
            self.cooldown_timer = settings.player.shot.cooldown

    def update(self, dt):
        """AAA"""
        self.cooldown_timer -= dt

        """AAA"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

class Shot(CircleShape):
    """AAA"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """AAA"""
        pygame.draw.circle(screen, (settings.player.shot.color), self.position, self.radius, settings.player.shot.thickness)

    def update(self, dt):
        """AAA"""
        self.position += self.velocity * dt