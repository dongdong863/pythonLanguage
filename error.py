#!/usr/bin/python
#coding:utf-8
#语法错误：漏打符号或者编写程序错误
#异常Exception：语句或者表达式在语法上是正确的，但是执行是可能会导致错误，比如字段只有3个键，取第4个，执行时会报错

#TypeError、IndexError、keyError、ZeroDivisionError

#FileNotFoundError找不到文件产生的异常
#文件夹下有read.txt，只输入read，就会报错，python并不知道read文件是说明
# file_name = input("请输入文件名：")
f = open(file_name)

#
