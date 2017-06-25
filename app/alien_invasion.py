import pygame
from pygame.sprite import Group

import app.game_rules as gr
import app.game_controls as gc
from app.settings import Settings
from app.ship import Ship
from app.game_stats import GameStats
from app.button import Button
from app.scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Draw the game elements
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # alien = Alien(ai_settings, screen)

    gr.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gc.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gr.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gr.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gr.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
