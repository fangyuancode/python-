1.作业原创

2.爬取招聘网上，前端工程师的招聘数据，对数据进行可视化分析。

3. a: 从招聘公司的布局情况，画出公司省份分布地图。
    b: 从招聘公司的学历要求，画出了招聘公司到的要求水球图。
    c.从招聘公司所在省份的平均工资，画出各个省份的平均工资柱状图。
    d:从招聘公司的公司性质占比，画出各个公司类型的饼状图。

4.数据可视化


一、 准备工作
绘图工具：
数据没有经过处理，那么他就只是一堆数据。

如果可能够将数据进行可视化操作，那数据它就可以很轻松的说明问题啦。
基于`Python`，`pyecharts`，`matplotib`，`seaborn`，。

二、模块安装

 pip install `pyecharts`

三、 数据获取
1. 数据预处理（数据清洗）
   主要使用`pandas`模块，
 2.  清理空值，去除重复项，将数据处理一致等，

四、 制作图表

1.导入模块
python
import jieba
import pandas as pd

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar, Map, WordCloud, Page

2、数据可视化，在对图表进行整合。
