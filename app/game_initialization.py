import pygame

import app.game_functions as gf


def begin_game(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        setup_game(ai_settings, aliens, bullets, sb, screen, ship, stats)
    else:
        end_game(stats)


def end_game(stats):
    stats.game_active = False
    pygame.mouse.set_visible(True)


def setup_game(ai_settings, aliens, bullets, sb, screen, ship, stats):
    pygame.mouse.set_visible(False)
    ai_settings.init_dynamic_settings()
    stats.reset_stats()
    stats.game_active = True
    sb.reset_scoreboard()
    reset_ship(bullets, ship)
    reset_fleet(ai_settings, aliens, screen, ship)


def reset_fleet(ai_settings, aliens, screen, ship):
    aliens.empty()
    gf.create_fleet(ai_settings, screen, ship, aliens)


def reset_ship(bullets, ship):
    bullets.empty()
    ship.center_ship()