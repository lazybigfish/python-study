import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(url)
response_dict = r.json()
print(response_dict['total_count'])
repo_dicts = response_dict['items']
""""遍历存储可视化的数据"""
names,owners,starts = [],[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    owners.append(repo_dict['owner']['login'])
    starts.append(repo_dict['stargazers_count'])
    # print('Repository:',repo_dict['html_url'])

""""开始可视化"""
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Mosr-Startrred Python Project On GitHub'
chart.x_labels=names
chart.add('',starts)
chart.render_to_file('pythin_repo.svg')