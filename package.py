#!/usr/bin/python
#coding:utf-8

#Package,创建一个文件夹，它的名字就是包的名字，包就是用来存放相关的模块
#文件夹里创建一个__init__.py的模块文件（python--package--__init__.py）
# 这个文件可以是空文件件，它告诉python把这个文件夹当作包来处理

import Package.hello as h
h.p()

import Package.singlemoudle as s
#调用模块时，那么这个模块就不是主程序，所以不会运行，测试代码
print(s.cal(1,2))
print(s.__name__)

#dir()和help()内置函数
#dir(list)可以告诉你list的所有属性和方法
#help(list.sort)可以看到具体的用法
# dir(list)
help(list.sort)