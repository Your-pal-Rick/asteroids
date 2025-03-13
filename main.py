import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    my_player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        my_player.update(dt)
        screen.fill((0,0,0))
        my_player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
