import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style = my_style,x_label_rotation = 45,show_legend=False)
chart.title = 'Python Project'
chart.x_labels = ['httpie','django','flask']
plot_dicts = [
    {'value':16101,'label':'description of httpie'},
    {'value':15208,'label':'description of djngo'},
    {'value':13401,'label':'description of flask'}
]
chart.add('',plot_dicts)
chart.render_to_file('bar_des.svg')
