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
# for red in range(0,4):
#     for white in range(0,4):
#         for black in range(2,7):
#             if red+white+black ==8:
#                 print(red,white,black)
# #统计
# n = 0
# for red in range(0,4):
#     for white in range(0,4):
#         for black in range(2,7):
#             if red+white+black ==8:
#                 print(red,white,black)
#                 n+= 1
# print(n)
#
# #设计一个验证用户密码的程序，用户只有3次机会
# count = 3
# pwd = 123456
# while count:
#     count -= 1
#     num = int(input("请输入密码"))
#     if num== pwd:
#         print("密码正确")
#         break
#     else:
#         if count !=0:
#             print("密码错误，你还有",count,'次机会')
#         else:
#             print('你已经输入3次错误密码，无法再次输入')
#
#
# #pow()乘法问题
# a =pow(2,3)
# print(a)
# #乘法做循环
# def power(x,y):
#     result = 1
#     for i in range(y):
#         result= result * x
#     return result
# print(power(2,4))
#
# #统计一个子字符窜在另一个字符窜中出现的次数
# #比如一个字符窜"Her name is Lily and she is cute",我们想知道is在你这个字符窜中出现了几次
#
# a = input("请输入字符窜：")
# b = input("请输入子字符窜（两个字符）")
# times = a.count(b)
# print("子字符窜一共在字符窜中出现了",times,"次")
#
#
# #列表专项训练
# #复制列表
# l1 = ["hello",'seven',["yr",["h","mike",'all']],123,456]
# l2 = l1[:]
# print(l2)
#
# #切片，list取值的一种方式，取值是---顾头不顾尾
#
# l=[1,2,3,4,5,6,7]
# l3=l[0:2]
#
# #list[起始：结束：步长]--默认部长是1
# #2是每隔一个数取一个值
# l4 = l[0::2]
# print(l4)
# #倒着去
# l5 = l[::-1]
# print(l5)
#
# #l1 = ["hello",'seven',["yr",["h","mike",'all']],123,456]输出
# l6 = ["hello",'seven',["yr",["h","mike",'all']],123,456]
# #a列表里的b列表里的c列表的元素有h
# n =l6[2][1][0]
# print(n)
#
# #循环中3个循环控制语句break,continue,pass
num = 0
while num<10:
    num +=1
    if num%2>0:
        continue
    print(num)
print('------------------')
num = 0
while True:
    print(num)
    num+=1
    if num >5:
        break
        
#创建通讯录
contact={'Lily':'123456','mike':'234567','lucy':'345678','cane':'456789'}
print('---欢迎进入通讯录---')
print('---1、查找联系人---')
print('---2、退出通讯录---')
while True:
    num = int(input('请输入查找的联系人：'))
    if num ==1:
        name = input('请输入联系人的名字：')
        if name in contact:
            print(name,contact[name])
        else:
            print('该联系人不存在')
        
    elif num ==2:
        break
print('感谢使用通讯录')

#写一个程序，接受用户输入的内容
filename = input('请输入文件的名字：')
context = input('请输入文件的内容')
f = open(filename,'w')
f.write(context)
f = open(filename,'r')
print(f.read())
f.close()


