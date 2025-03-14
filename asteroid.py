# Standard library imports
import random

# Third-party imports
import pygame

# Local application imports
from circleshape import CircleShape
from constants import settings # type: GameSettings

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, settings.color.outline, self.position, self.radius, settings.asteroid.thickness)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == settings.asteroid.min_radius:
            return
        
        rand_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - settings.asteroid.min_radius
        
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = vec1 * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2.velocity = vec2 * 1.2

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-settings.asteroid.max_radius, y * settings.screen.height),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                settings.screen.width + settings.asteroid.max_radius, y * settings.screen.height
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * settings.screen.width, -settings.asteroid.max_radius),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * settings.screen.width, settings.screen.height + settings.asteroid.max_radius
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > settings.asteroid.spawn_rate:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, settings.asteroid.kinds)
            self.spawn(settings.asteroid.min_radius * kind, position, velocity)