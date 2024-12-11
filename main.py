import pygame
from constants import *

def main():
    # initiate pygame
    pygame.init()
    # set screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()