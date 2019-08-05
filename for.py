#!/usr/bin/python
#coding:utf-8
nums = [10,9,8,7]
for num in nums:
    print(num)

colors = ['red','yellow','blue']
for c in colors:
    print(c)
#缩进
colors = ['red','yellow','blue']
for c in colors:
    print(c)
print('I like them all')

nums = [10,9,8,7,6]
for num in nums:
    print(num)
    print('numbers')

#range--范围，range(1,5)左闭又开的意思，（1，2，3，4）
for value in range(1,5):
    print(value)

for num in range(3,6):
    print(num)


#range制作列表
nums = list(range(1,5))
print(nums)

for value in range(5,6):
    print("what's your name")

nums = [13,71,24,61]
for num in nums:
    print(num)
print('are,numbers')

#用range()制作1～6个数字范围
for i in range(1,7):
    print(i)
#用range()制作一个包含14～16这三个元素的列表
f = list(range(14,17))
print(f)

#用range()将"I love you "输入三遍
for str in range(1,4):
    print('I love you')

