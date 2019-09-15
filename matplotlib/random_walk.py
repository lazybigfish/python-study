from random import choice
#导入choice()来为每次决策做出选择

class RandomWalk():
    def __init__(self,num_points = 5000):
        self.num_potins = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """"计算随机漫步的所有点"""
        #建立循环不断漫步，直到达到了列表的指定长度
        while len(self.x_values) < self.num_potins:
            #决定前进方向以及沿着方向前进的距离
            #判断x轴的方向
            x_direction = choice([1,-1])
            #判断X轴的前进步数
            x_distance = choice([0,1,2,3,4])
            #得出x的坐标轴点，下方y轴一样的取值方法
            x_step = x_direction * x_distance
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #如果取出的值为0，就执行下一次的循环
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
