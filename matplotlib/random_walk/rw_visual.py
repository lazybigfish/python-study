import matplotlib.pyplot as plt
from random_walk.random_walk import RandomWalk

#实例话一个漫步类
# rw  = RandomWalk()
# #执行内部漫步函数
# rw.fill_walk()
#
# plt.scatter(rw.x_values,rw.y_values,s = 15)
# plt.show()

""""多次漫步运行在一张图，用while语句循环，并设置停止条件"""

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    #设置输出绘图的窗口大小
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_potins))
    plt.scatter(rw.x_values,rw.y_values,c = point_numbers,cmap=plt.cm.Blues,edgecolors='none',s = 1)
    #设置原点
    plt.scatter(0,0,c = 'yellow',edgecolors='none',s = 100)
    #设置终点显示
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c = "red",edgecolors='none',s = 100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("keep going?(y/n):\n")
    if keep_running == 'n':
        break

