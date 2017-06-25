from time import sleep

import pygame

import app.game_initialization as gi


# Game Rules
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if bullet hit alien and increase level, speed, and score when fleet is destroyed"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            increase_score(ai_settings, aliens, sb, stats)
        check_high_score(stats, sb)
    if len(aliens) == 0:
        start_new_level(ai_settings, aliens, bullets, sb, screen, ship, stats)


def increase_score(ai_settings, aliens, sb, stats):
    """Increase score when alien is shot"""
    stats.score += ai_settings.alien_points * len(aliens)
    sb.prep_score()


def start_new_level(ai_settings, aliens, bullets, sb, screen, ship, stats):
    """Start new level when fleet is destroyed"""
    bullets.empty()
    ai_settings.increase_speed()
    stats.level += 1
    sb.prep_level()
    gi.create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats, sb):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        gi.reset_ship(bullets, ship)
        gi.reset_fleet(ai_settings, aliens, screen, ship)
        sleep(0.5)
    else:
        stats.game_active = False


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if the fleet is at an edge, and then update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)


# Screen handling
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    sb.show_scoreboard()

    if not stats.game_active:
        play_button.draw_button()

    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()
