import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

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

    my_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
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

        screen.fill((0,0,0))

        for member in drawable:
            member.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
