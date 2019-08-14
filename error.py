#!/usr/bin/python
#coding:utf-8
#语法错误：漏打符号或者编写程序错误
#异常Exception：语句或者表达式在语法上是正确的，但是执行是可能会导致错误，比如字段只有3个键，取第4个，执行时会报错

#TypeError、IndexError、keyError、ZeroDivisionError

#FileNotFoundError找不到文件产生的异常
#文件夹下有read.txt，只输入read，就会报错，python并不知道read文件是说明
# file_name = input("请输入文件名：")
# f = open(file_name)

#处理异常
# try：
#     #检测范围
# except Exception[as reson]:
#     #出现异常后的处理

# f = open('file.txt')
# print(f.read())
# f.close()
#找不到文件异常
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('文件出错了')

#0 不能做除数异常
try:
    num1=input('请输入被除数：')
    num2=input('请输入除数：')
    result = int(num1)/int(num2)
    print(result)
except ZeroDivisionError:
    print('0不能做除数')

#查看具体出错原因
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError as reason:
    print('出错的原因：'+str(reason))