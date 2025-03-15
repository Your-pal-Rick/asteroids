"""
Asteroids Game - Player module

Contains the Player class, which handles player inputs, position, movement, drawing,
updating, shooting, collisions, and game quit by pushing Esc.
Contains the Shot class, which handles shot position, velocity, collisions, drawing,
and updating.

Both inherit attributes and methods from the CircleShape class.

Imported by Game module.
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Local application imports
from constants import settings # type: GameSettings
from circleshape import CircleShape

class Player(CircleShape):
    """Player class, inheriting attributes and methods from parent CircleShape.
       Handles player ship position, velocity, rotation, movement, shooting,
       sync to update rate (via game.dt), and keyboard inputs.
    """
    def __init__(self, x, y):
        """Inherit CircleShape class attributes and methods.
            Sets rotation and shooting cooldown values."""
        super().__init__(x, y, settings.player.radius)
        self.rotation = 0
        self.cooldown_timer = 0

    def triangle(self):
        """Returns list of three vector lines using instance radius and rotation."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        """Draw method to be called for drawables in Game draw method.
           Draws instance triangle on game screen using player color and line thickness settings."""
        pygame.draw.polygon(screen, (settings.player.color), self.triangle(), settings.player.thickness)

    def rotate(self, dt):
        """Rotate method to be called in player inputs.
           Adjusts instance rotation by turn_speed setting, regulated by dt."""
        self.rotation += settings.player.turn_speed * dt

    def move(self, dt):
        """Move method to be called in player inputs.
           Adjusts instance position using rotated forward vector multiplied by player speed setting regulated by dt."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * settings.player.speed * dt

    def shoot(self):
        """Shoot method to be called in player inputs.
           Checks if cooldown timer is up, then produces Shot instance in front of ship position.
           Uses shot radius setting and player instance rotation to set velocity, then sets timer to cooldown setting."""
        if self.cooldown_timer <= 0:
            shot = Shot(self.position[0], self.position[1], settings.player.shot.radius)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * settings.player.shot.speed
            self.cooldown_timer = settings.player.shot.cooldown

    def update(self, dt):
        """Update method to be called for updatables group in Game update method."""
        # Reduces shoot cooldown by dt
        self.cooldown_timer -= dt

        """Handles player inputs and associated actions using previously defined methods."""
        keys = pygame.key.get_pressed()
        # A: Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # D: Rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)
        # W: Fly forward
        if keys[pygame.K_w]:
            self.move(dt)
        # S: Fly backward
        if keys[pygame.K_s]:
            self.move(-dt)
        # Space: Shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
        # Esc: Exit game
        if keys[pygame.K_ESCAPE]:
            sys.exit(settings.exit_m.manual)

class Shot(CircleShape):
    """Shot class, inheriting attributes and methods from CircleShape class.
       Handles shot radius, position, velocity, collisions, drawing, and updating."""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw method to be called for drawables in Game draw method.
           Draws instance circle on game screen using shot color and line thickness settings."""
        pygame.draw.circle(screen, (settings.player.shot.color), self.position, self.radius, settings.player.shot.thickness)

    def update(self, dt):
        """Update method to be called for updatables group in Game update method.
           Handles shot velocity regulated by dt."""
        self.position += self.velocity * dt