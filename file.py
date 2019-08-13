#!/usr/bin/python
#coding:utf-8
#内置函数open()
#打开一个文件
#打开一个参数，标识我要打开的文件名为python.txt
#第二个参数，表示打开文件的模式是w，
# 表示打开文件的模式是ww打开一个文件只用于写入，如果该文件已存在则打开文件
# 并从头开始编辑，即原有内容被删除，
# 如果该文件不存在，穿件新文件
#open()后会返回一个对象，file = open()把这个对象保存在file
file =open('F:/pythonlanguage2/cxy/test.txt','w')
file.close()
print('文件名称',file.name)
print('文件是否关闭',file.closed)
print('文件访问模式',file.mode)
f = open('F:/pythonlanguage2/cxy/test.txt','r')
print(f)

