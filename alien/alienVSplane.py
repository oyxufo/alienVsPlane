
import sys
import pygame
from alie import Alien
from pygame.sprite import Group
from game_stats import GameStats
from ship import Ship
from settings import Settings
import game_function as gf
from button import Button
from scorebord import Scoreboard
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("打倒黑恶势力")
    play_button = Button(ai_settings,screen,"来Van吧")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    sb = Scoreboard(ai_settings,screen,stats)
    

    while True:
        gf.check_event(ai_settings,screen,ship,bullets,stats,play_button,aliens)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,aliens,bullets,ship,screen,stats,sb)
            gf.update_aliens(aliens,ai_settings,ship,bullets,stats,screen)
            
            #print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb)
       
    
run_game()
