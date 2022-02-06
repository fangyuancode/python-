# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:49:25 2021

@author: bin
"""
import pandas as pd
# 4.柱状图
list1=['重庆','浙江','云南','四川','上海','陕西','山东','辽宁','江西','江苏','湖南'
,'湖北','河南','河北','海南','贵州','广西','广东','北京','安徽']

dataframe = pd.DataFrame(list1)
# dataframe.to_excel('list.xls')
# print(dataframe)
    
list2 = [13.8,16.3,22.5,10.5,17.5,12.2,12,14,13.5,12,10.9,13.1,12.5,7.5,11.5,10,17,15,20,15]
output_excel = {'省份':list1, '平均工资（k）':list2}

output = pd.DataFrame(output_excel)
output.to_excel('柱状图.xlsx', index=False)