import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """description of class"""
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #设置一个运动标志
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        self.centerx = float(self.rect.centerx)
    #判断
    def update(self):
        if self.moving_right == True and self.rect.right<self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        if self.moving_left == True and self.rect.left>0:
            self.centerx -= self.ai_settings.ship_speed
        self.rect.centerx = self.centerx
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx


        


