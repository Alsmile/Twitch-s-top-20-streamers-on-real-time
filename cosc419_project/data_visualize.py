# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4 22:58:28 2020

@author: aaron
"""

import json
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

file_path = 'repos.json'
with open(file_path) as f:
    repo_dicts = json.load(f)

names, views = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    views.append(repo_dict['view'])


my_style = LS('#800000', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 20
my_config.label_font_size = 16
my_config.major_label_font_size = 16
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Top 20 English speaking streamers on twitch.tv in real time'
chart.x_labels = names
chart.add('', views)
chart.render_to_file('data_chart.svg')