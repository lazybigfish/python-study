import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
#通过设置c和cmap来调整映射的颜色变化
plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Blues,s=40)
#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()