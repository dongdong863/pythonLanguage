#!usr/bin/python
#coding:utf-8

#def()函数，全称：define
# def +函数名()+英文标点符号的括号，第二行要缩进

def Hello():
    print('Hello')
    return

Hello()

def greet():
    print('Nice to meet you !')
    return

greet()

def  intro():
    print('I come from China')
    return
intro()

#录入同学的信息：姓名，年龄，学号
def printinfo(name,age,ID):
    print("姓名",name)
    print("年龄",age)
    print("学号",ID)
    return
printinfo('xiao',12,1)

#定义一个传入字符窜的函数
def printme(str):
    print(str)
    return
printme("你好")

#定义一个传入整数的函数
def printme(int):
    print(int)
    return
print(1)

#定义多个函数
#定义一个函数做加法
import math
def plus(a,b):
    return a +b
plus(1,2)

#定义一个函数将3个数字相乘
def mul(a,b,c):
    return a*b*c

print(mul(1,2,3))

#局部变量和全局变量
#y是定义在函数里面的交局部变量
#局部变量是在某个函数中声明的，只能在该函数中调用它
#a是全局变量，全局变量是在整个py文件中声明，全局范围内可以访问

def pllus(a,b):
    y = a+b
    return y
a = plus(3,4)
print(a)


#定义一个函数plus()，并调用 plus()将数字7和8相加得到结果

def plus(a,b):
    x = a+b
    return x
y = plus(7,8)
print(y)

#定义一个又三个参数的函数mul()，然后调用mul()计算4，8，10的乘积

def mul(a,b,c):
    x = a*b*c
    return x
y = mul(2,3,4)
print(y)