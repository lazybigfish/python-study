import matplotlib.pyplot as plt

#设置显示的数据
squares = [1,4,9,16,25]
#设置y刻度的值
input_values = [1,2,3,4,5]
#引入数据显示，并且设置线条粗细程度
plt.plot(input_values,squares,linewidth = 5)
#设置标题
plt.title("Square Numbers",fontsize = 24)
#设置x坐标标签以及大小
plt.xlabel("Value",fontsize = 14)
#设置y坐标标签以及大小
plt.ylabel("Square of Value",fontsize =14)
#设置刻度的显示样式
plt.tick_params(axis='both',labelsize = 14)
plt.show()