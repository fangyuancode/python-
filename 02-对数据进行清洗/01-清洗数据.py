# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:07:29 2021

@author: bin
"""
# import re
import pandas as pd

df = pd.read_excel('./web前端招聘数据.xlsx')
# print(df['城市'])

location_list=[]
# # 1.对城市进行处理
for location in df['城市']:
    data = str(location).split('-')[0]
    location_list.append(data)
# print(location_list)    

# # 替换
df['城市'] = location_list

# print(df)

# 2.公司规模进行处理

company_list=[]
for number in df['公司规模']:
    if '少于' in str(number):
          number.strip('少于')
    if '-' in str(number):
        data = number.split('-')[1]
          # print(data)
    if '人' in data:
        data1=data.strip('人')
        # print(data1) 
        company_list.append(data1)
# print(company_list)
company_list.append(500) 
company_list.append(100)
company_list.append(1000)     
df['公司规模'] = company_list     


# 3.处理招聘人数
index=0
company_num=[]
for number in df['招聘人数']:
    if '人' in str(number):
            data1=number.strip('人')
            index+=1
            # print(index)
            if '招' in data1:
                data2=data1.strip('招')
            company_num.append(data2)
                    
print(company_num[48]) 
print(company_num) 
df['招聘人数'] = company_num

# # 4.处理工资
company_money=[]
for number in df['薪资']:
    if '万/月' in str(number):
            data1=number.strip('万/月')
    # print(data1)
    if '-' in data1:
        num1=data1.split('-')[0]
        a = float(num1) * 10
        num2=data1.split('-')[1]
        b = float(num2) * 10
        c = (a+b)/2
        # print(c)
        company_money.append(c)
# print(company_money)
        
df['薪资'] = company_money       
       
    

# # 5.添加到新的excel表
df.to_excel('清洗后的数据1.xlsx',index=None)

























