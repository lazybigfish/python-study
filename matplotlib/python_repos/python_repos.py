import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(url)
response_dict = r.json()
print(response_dict['total_count'])
repo_dicts = response_dict['items']
""""遍历存储可视化的数据"""
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # owners.append(repo_dict['owner']['login'])
    # starts.append(repo_dict['stargazers_count'])
    #建立一个集合装标签详细信息
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
    }
    plot_dicts.append(plot_dict)
    # print('Repository:',repo_dict['html_url'])

""""开始可视化"""
my_style = LS('#333366',base_style=LCS)
# chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)
#创建一个Pygal的config的实例，来集中定制图标的外观
my_config = pygal.Config()
#x轴的标签旋转45度
my_config.x_label_rotation = 45
#是否展示图例
my_config.show_legend = False
#标题字体大小
my_config.title_font_size = 24
#标签字体大小
my_config.label_font_size = 14
#主标签字体大小
my_config.major_label_font_size = 18
#字符长度控制在15个最多
my_config.truncate_label = 15
#是否显示图标种水平线
my_config.show_y_guides = False
#自定义图标宽度
my_config.width = 1000
chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Mosr-Startrred Python Project On GitHub'
#x轴标签
chart.x_labels=names
#添加数据
chart.add('',plot_dicts)
chart.render_to_file('pythin_repos1.svg')