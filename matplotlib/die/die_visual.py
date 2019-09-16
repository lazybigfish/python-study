from die.die import Die
import pygal

""""新建一个实例"""
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
#新建一个空列表存储个数出现的次数
frequencies = []

for value in range(1,die.num_sides+1):
    #计算个数出现的次数
    frequency = results.count(value)
    #出现的次数存入空列表
    frequencies.append(frequency)
#对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 100 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Results'
hist.y_title = 'Frequenrcy of Result'
hist.add("D6",frequencies)
hist.render_to_file('die_visual.svg')
