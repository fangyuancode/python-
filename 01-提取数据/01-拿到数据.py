# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:27:43 2021

@author: bin
"""
import re
import requests
from bs4 import BeautifulSoup
import json
import csv
import pprint#格式化输出模块

#3.接受新数据

f=open('web前端招聘数据1.csv',mode='a',encoding='gb2312',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
   '标题',
   '公司名字',
   '城市',
   '薪资',
   '学历',
   '经历',
   '招聘人数',
   '公司类型',
   '公司规模',
   '公司详情页',
   '招聘发布时间',
    ])

csv_writer.writeheader()#写入表头数据
# 1.拿数据
url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,21.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# url="https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,20.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
resp=requests.get(url,headers=header)
# resp.encoding='utf-8' 
# resp.decode('utf-8').encode('utf-8')
# print(resp)

html=resp.text
# print(resp.cookies)

# print(html)
# soup = BeautifulSoup(html,"lxml")#list类型
# content=soup.find("div","class_=cn")
# print(content)
html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>',resp.text)[0]

# print(html_data)
# 把字符串转成字典

json_data = json.loads(html_data)
# print(type(json_data))

pprint.pprint(json_data['engine_jds'])

# 字典取值，
for index in json_data['engine_jds']:
    dict = {
        '标题':index['job_name'],
        '公司名字':index['company_name'],
        '城市':index['workarea_text'],
        '薪资':index['providesalary_text'],
        '学历':index['attribute_text'][2],
        '经历':index['attribute_text'][1],
        # '招聘人数':index['attribute_text'][3],
        '公司类型':index['companytype_text'],
        '公司规模':index['companysize_text'],
        '公司详情页':index['company_href'],
        '招聘发布时间':index['issuedate'],
          }
    # csv_writer.writerow(dict)
    print(dict)


resp.close()
















