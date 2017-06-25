import pygame

from app.alien import Alien


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


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + ai_settings.alien_space * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 5 * alien_width
    number_aliens_x = int(available_space_x / (ai_settings.alien_space * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (4 * alien_height) - ship_height)
    number_rows = int(available_space_y / (3 * alien_height))
    return number_rows


def reset_fleet(ai_settings, aliens, screen, ship):
    aliens.empty()
    create_fleet(ai_settings, screen, ship, aliens)


def reset_ship(bullets, ship):
    bullets.empty()
    ship.center_ship()