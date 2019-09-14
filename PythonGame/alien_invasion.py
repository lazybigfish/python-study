
import pygame

#设置文件导入
from settings import Settings
#飞船图像文件
from ship import Ship
#推出按钮事件响应倒入
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #创建
    ai_settings = Settings()
    #新建一个屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建飞船
    ship = Ship(ai_settings,screen)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标的事件
        gf.check_events(ship)
        #每次循环重绘屏幕填充颜色
        gf.update_screen(ai_settings,screen,ship)

run_game()