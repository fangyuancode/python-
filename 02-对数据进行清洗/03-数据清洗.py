# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:29:21 2021

@author: bin
"""
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

import pandas as pd

df = pd.read_excel('./web前端招聘-可视化数据.xlsx')
location_list=[]
# # 1.对城市进行处理
for location in df['省份城市']:
    data = str(location).split('-')[0]
    location_list.append(data)
# print(location_list)    

# # 替换
df['省份城市'] = location_list
print(df)
df.to_excel('最终可视化数据.xlsx',index=None)
# data = df['省份城市'].value_counts().items()
# for it in data:
#     print(it)
# print(data)
# map = (
#     Map()
#     .add("招聘平均薪资",[['广东',100],['广西',100],['湖南',19,]], "china")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="商家店铺地址分布图"),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     )
#     .render("地图.html")
# )




























