# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:58:12 2021

@author: bin
"""

import pandas as pd

df = pd.read_excel('./清洗后的数据-可视化.xlsx')
print(df)
df.drop_duplicates(inplace=True)

print(df)
df.to_excel('可视化数据.xlsx',index=None)