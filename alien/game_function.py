
import sys
import pygame
import random
from bullet import Bullet
from alie import Alien
from random import randint
from pygame.sprite import Group
from time import sleep
def check_event(ai_settings,screen,ship,bullets,stats,play_button,aliens):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                if event.key == pygame.K_SPACE:
                    if len(bullets) <ai_settings.bullets_allowed:
                        new_bullet = Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(stats,play_button,mouse_x,mouse_y,screen,ai_settings,ship,aliens,bullets)
                    
                    

def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active :
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_settings,aliens,bullets,ship,screen,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()
    if len(aliens) == 0:
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,aliens,ship)

    

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height-(3 * alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

def create_alien(aliens,screen,alien_number,ai_settings,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x 
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(randint(3,number_alien_x)):
            create_alien(aliens,screen,alien_number,ai_settings,row_number)
    
def update_aliens(aliens,ai_settings,ship,bullets,stats,screen):
    check_alien_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

def check_alien_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(ai_settings,aliens)
            break

def change_alien_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >=screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break


def check_play_button(stats,play_button,mouse_x,mouse_y,screen,ai_settings,ship,aliens,bullets):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()