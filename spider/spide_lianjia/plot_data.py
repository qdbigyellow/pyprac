import requests
import pandas as pd
from pyecharts import Pie
from pyecharts import Bar

def draw_bar(thing):
    data = pd.read_csv(thing+'.csv', encoding='utf_8_sig')
    rental = list(data['面积'])
    area = list(data['月租金'])
    bar = Bar()
    bar.width = 2000
    bar.add("rent apt",   # instruction
            rental, # X-axis
            area,   # Y-axis
            xaxis_rotate = 35,
            xaxis_intevale = 0,
            label_color = "read",
            is_random = False)
    bar.render()

def draw_pie(thing):
    data = pd.read_csv(thing+'.csv', encoding='utf_8_sig')
    level = list(data['楼层'])
    oritation = list(data['房屋朝向'])
    pie = Pie()
    pie.add("", oritation, level,
            radius=[40, 75],
            legend_oriente="vertical")
    pie.render()


def main():
    draw_bar(r"spide_lianjia\data")
    draw_pie(r"spide_lianjia\data")


if __name__ == '__main__':
    main()