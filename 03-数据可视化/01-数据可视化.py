# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:29:21 2021

@author: bin
"""
from pyecharts import options as opts
from pyecharts.charts import Map


import pandas as pd
from pyecharts.charts import Bar

df = pd.read_excel('./最终可视化数据.xlsx')
locations=[]
data = df['省份城市'].value_counts().items()
for it in data:
    # print(it)
    locations.append(it)
locations.append(('福建', 20))
locations.append(('甘肃', 20))
locations.append(('新疆', 2))
locations.append(('青海', 2))
locations.append(('内蒙古', 5))

# print(locations)
# 1.招聘公司分布图
map1= (
    Map()
    .add("招聘公司数量",[list(location) for location in locations], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="招聘公司地址分布图"),
        visualmap_opts=opts.VisualMapOpts(max_=500),
    )
    .render("1-招聘公司分布地图.html")
)

# 2.学历要求图
# 本科，221 专科：142
from pyecharts import options as opts
from pyecharts.charts import Liquid

liquid = (
    Liquid()
    .add("本科占比", [0.54,0.55])	
 	# 第一个值为显示的值，第二个值为水的分量
    .set_global_opts(title_opts=opts.TitleOpts(title="本专科学历要求占比"))
    .render("2-学历占比.html")
)

# # 3.多饼图
data = df['公司类型'].value_counts().items()
# # print(data)

from pyecharts.charts import Pie

# print(it for it in data)    
    
    
pie = (
    Pie()
    .add("", [it for it in data])
    .set_global_opts(title_opts=opts.TitleOpts(title="公司占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("3-公司类型占比图.html")
)
# # print(list(z) for z in zip(Faker.choose(), Faker.values()))

# 4.柱状图
df = pd.read_excel('./柱状图.xlsx')
# 4.柱状图
# print(df['省份'])
# print(df['平均工资（k）'])

bar = (
    Bar()
    .add_xaxis([it for it in df['省份']])
    .add_yaxis("招聘工资（k）", [it for it in df['平均工资（k）']])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各省份招聘平均工资(K)"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("4-招聘平均工资.html")
)











