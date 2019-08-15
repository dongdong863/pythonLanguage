#!/usr/bin/python
#coding:utf-8

# num = int(input('请输入1到100之间的数：'))
# if num >=1:
#     print('在范围内')
# elif num>100:
#     print('在范围外')
# else:
#     print('在范围外')

# num=list(range(1,101))
# for i in num:
#     if i%2!=0:
#         print(i)
#
# year = int(input('输入年份：'))
# if year %4==0 and year %100!=0:
#     print('这个年份是闰年')
# else:
#     print('这个年份非闰年')
#
#一个口袋放了12个球，红白球各3个，黑球6个，从中任取8个共有多少种不同颜色的搭配
#3+3+2、1+1+6，确定好最大最小值
for red in range(0,4):
    for white in range(0,4):
        for black in range(2,7):
            if red+white+black ==8:
                print(red,white,black)
#统计
n = 0
for red in range(0,4):
    for white in range(0,4):
        for black in range(2,7):
            if red+white+black ==8:
                print(red,white,black)
                n+= 1
print(n)










