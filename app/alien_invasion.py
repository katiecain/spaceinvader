import pygame
from pygame.sprite import Group

from app.settings import Settings
from app.ship import Ship
import app.game_functions as gf


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Draw the game elements
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # alien = Alien(ai_settings, screen)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
