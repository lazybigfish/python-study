import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """"初始化飞船，并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像
        self.image =pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #定义新的属性存储
        self.center = float(self.rect.centerx)
        #默认移动状态是无
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            #更新飞船的center指数，而不再是rect
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        #根据center指数更新rect
        #如果移动值未触及界面的临界值将继续
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center-= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center




    def blitme(self):
        self.screen.blit(self.image,self.rect)

