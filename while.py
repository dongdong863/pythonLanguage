#!/usr/bin/python
#coding:utf-8
#while循环结构
#while条件：
    #执行
#while结构现实1-7个数字
a = 1
while a<=7:
    print(a)
    a = a+1
#利用while循环现实8～1，从8开始至1的八个数字
a=8
while a>0:
    print(a)
    a= a-1
#利用while结构显示50至1之间的所有偶数
a = 50
while a>0:
    if a%2==0:
        print(a)
    a = a-1

while a>0:
    print(a)
    a=a -2


#累乘数字11至15
num = 11
mul=1
while num<=15:
    mul = mul*num
    num = num+1

print(mul)


#while求列表里的平均数
list=[2,9,7]
sum =0
i = 0
while i <len(list):
    sum =sum+list[i]
    i = i+1
ave = sum/len(list)
print(ave)

#已知列表list=[6,1,2,9,2],求平均值
list =[6,1,2,9,2]
sum = 0
i = 0
while i <len(list):
    sum = sum +list[i]
    i = i+1
ave= sum /len(list)
print(ave)



#用while求一个列表里1至9数字的平均数
# num = list(range(1,10))
# while i



#显示0至50的偶数(不包括50)
# while 结构确保a的范围是从0-50
# if结构确保a%2==0，a是偶数
i=0
while i<50:
    if i%2 ==0:
        print(i)
    i = i+1

a =0
while a <50:
    print(a)
    a=a+2

#已知列表list=[45,34,52],求平均值
list=[45,34,52]
sum =0
i =0
while i<len(list):
    sum =sum +list[i]
    i =i+1
print(sum)

sum1=0
for i1 in list:
    sum1 = sum1+i1
print(sum1)