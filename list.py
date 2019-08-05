#!/usr/bin/python
#coding:utf-8

color = ['rea','green','blue']
message = 'My favourite color is :'+color[0]+'.'

print(message)
#——--------------------------------------------------

#更改列表元素的值
appearance = ['old','young','tall','short','thin']
print(appearance)
appearance[3]='fit'
print(appearance)

expression = ['cry','laugh','sad','happy','angry']
print(expression)
expression[2]= 'joy'
print(expression)
#--------------------------------------------------------
#在列表添加一个新元素--列表名.append()
family=['mom','dad','me','beibei']
print(family)
#妈妈想在养一只小猫咪
family.append('miaomiao')
print(family)

a = [10,11,12,13]
a.append(14)

furniture = ['door','window','table','chair']
print(furniture)
furniture.append('bed')
print(furniture)
#---------------------------------------------------------
#删除列表元素
#一盒巧克力吃掉一个椰子味的
chocolate = ['coconut','almond','original','coffee']
print(chocolate)
chocolate.remove('coconut')
print(chocolate)
chocolate.remove('original')
print(chocolate)
chocolate.remove('almond')
print(chocolate)
chocolate.remove('coffee')
print(chocolate)

vegetables = ['eggplant','tomato','potato','cucumber']
print(vegetables)
vegetables.remove('tomato')
print(vegetables)

animals = ['tiger','lion','monkey','deer']
print(animals)
animals.remove('tiger')
print(animals)

