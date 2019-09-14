class Settings():
    """"存储游戏的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕的设置，大小以及背景色
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        self.ship_speed_factor = 1.5