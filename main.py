import pygame
from constants import *
from player import Player


def main():
    pygame.init() # initiate pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set screen dimensions
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
