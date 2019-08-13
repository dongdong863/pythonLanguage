#!/usr/bin/python
#coding:utf-8

#Moudle把类似功能的代码写在一个模块里，这样整体代码就更清楚了
#日历模块 calendar
#导入模块的目录需要跟建立的这个.py文件是同个目录下（比如都是在F:/python/）
#模块名很长，可以变简洁一些，import 模块名 as 新名字  这一形式来导入模块

import calendar
import Hello as h
print(calendar)

#直接使用木块里的函数会报错，我们需要指定函数的来源，就像不同的班级都有叫小明的人，需要说清楚是哪个班的小明
#在方法名前面加上模块名，形成【模块名.函数】的形式
#hi()
h.hi()

#如果模块中有很多函数，但是只需要用到其中一个或几个，可以用from...import...的形式
#调用函数的时候就可以不用再说明模块了
from Hello import hi
hi()

#从模块中引入所有函数，那就用from...import*(这种写法一般不推荐，程序很多时，这样写容易出错)
from Hello import*
say()

#calendar模块中又一个month的函数，调用这个含函数传入年和月两个参数，比如2019年8月
date=calendar.month(2019,8)
print(date)


#导入一个不在同一目录下的模块--用到sys模块里的path来显示
#导入某个路径下的py文件,添加一个搜索路径！主要用两个\\
import sys
s=sys.path
print(s)
sys.path.append("F:\\python")