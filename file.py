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
# file =open('F:/pythonlanguage2/cxy/test.txt','w')
# file.close()
# print('文件名称',file.name)
# print('文件是否关闭',file.closed)
# print('文件访问模式',file.mode)
# f = open('F:/pythonlanguage2/cxy/test.txt','r')
# print(f)
import chardet
import os
# data =open(r"/Users/xudongma/python/pythonLanguage/cxy/python.txt", "rb").read()
file = open('/Users/xudongma/python/pythonLanguage/cxy/python.txt','r',encoding='GB2312')
# print(chardet.detect(data))
s = file.read()
#\n充当回车键
print('文件的内容是:\n',s)

#往文件里写内容,会覆盖原来的内容
file = open('/Users/xudongma/python/pythonLanguage/cxy/python.txt','w',encoding='GB2312')
s = file.write('i am learning python.\nI loge python')
file.close()

#格式：file = open("文件路径\\文件名"，"w")

#修改文件（改名rename("原来的名字"，"修改后的名字")）
# os.rename("Users/xudongma/python/pythonLanguage/cxy/python.txt","python2.txt")

#删除这个文件（remove("要删除的文件名")）
os.remove("Users/xudongma/python/pythonLanguage/cxy/python.txt")
