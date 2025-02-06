import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    #Start pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0

    new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20)

    #Main Loop
    while True:
        print("Game loop start")

        new_player.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

        Clock.tick(60)
        dt = (Clock.tick() // 1000)
        print("Game loop End")

if __name__ == "__main__":
    main()
