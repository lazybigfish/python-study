import sys
import pygame

"""独立出来一个函数检测按键的按下和起来"""
def check_keydown_events(event,ship):
    """"响应按下"""
    if event.key == pygame.K_RIGHT:
        # 如果按下来的是右键，那么ship方法的向右移动就是正确的
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    """"响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """"响应按键和鼠标操作事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #检测按键是否按下
        elif event.type == pygame.KEYDOWN:
            #如果按下了检测按下的是不是右键
            check_keydown_events(event,ship)
        #检测按键是否弹出
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship):
    """"更新屏幕图像"""
    # 每次循环重绘屏幕填充颜色
    screen.fill(ai_settings.bg_color)
    # 让飞船在图像上可见
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()