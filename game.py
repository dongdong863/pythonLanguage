#!/usr/bin/python
#coding:utf-8
#猜数字游戏，在1-10 之前随机一个数，用户输入1个数来猜测（只能猜一次）
# import random
# number = random.randint(1,10)
# print(number)
# print('我正在想找一个1到10之间的整数')
# print('猜猜看，这个数字是：')
# guess = int(input())
# if guess ==number:
#     print('恭喜你，猜对了！')
# else:
#     print('很遗憾，你猜错了！')
#猜数字游戏，在1-10 之前随机一个数，用户输入1个数来猜测（可循环猜10测）
import random
number = random.randint(1,10)
print(number)
print('我正在想找一个1到10之间的整数')
print('猜猜看，这个数字是：')
for i in range(1,11):
    print('猜猜看，这个数字是：')
    guess = int(input())
    if guess < number:
        print('太小1了')
    elif guess >number:
        print('太大了')
    else:
        print('恭喜你，猜中了')
        break
#break跳出整个for循环，
#在不满足上述两个条件时，用break跳出整个for循环，不再进行循环

#统计猜多少次
number = random.randint(1,10)
print(number)
print('我正在想找一个1到10之间的整数')
print('猜猜看，这个数字是：')
for i in range(1,11):
    print('猜猜看，这个数字是：')
    guess = int(input())
    if guess < number:
        print('太小1了')
    elif guess >number:
        print('太大了')
    else:
        print('猜对了，你总共猜了'+str(i)+'次数')
        break
print('游戏结束')