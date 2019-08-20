#!/usr/bin/python
#coding:utf-8
#datetime模块处理时间和日期
#datetime模块还包含了一个datetime类

from datetime import datetime,timedelta
now = datetime.now()
print(now)

#获取指定时间和日期创建datetime
t = datetime(2018,8,8,12,00)
print(t)

#用户输入的日期和时间都是字符窜，把字符窜转换为datetime
#用datetime.strptime()来实现
#规定日期和时间的格式
day = datetime.strptime('1997-07-01 00:00:00','%Y-%m-%d %H:%M:%S')
print(day)

#将datetime转换为字符窜 通过strftime()实现
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

#datetime库还定义了时间间隔对象（timedelta）
#一个时间点间隔加上一个时间间隔可以得到一个新的时间点
#上午3点加上5个小时，就是今天上午8点--import timedelta

now = datetime.now()
n = now +timedelta(hours=1)
print(n)
m = now - timedelta(hours=5)
print(m)
l = now +timedelta(days=2,hours=1)
print(l)