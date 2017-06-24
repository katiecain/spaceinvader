import sys

import pygame


def run_game():
    # Initializegame and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color=(230, 230, 230)

    # Start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.fill(bg_color)

    # Make the most recent drawn screen visible
        pygame.display.flip()

run_game()