#!/usr/bin/python
#coding:utf-8
#累加：求元素的和
sum = 0
nums = [11,23,53,24,5]
for num in nums:
    sum = sum +num
print(sum)

sum= 0
nums = list(range(1,11))
for num in nums:
    sum = sum + num
print(sum)

#len()函数，求元素的个数

sum = 0
nums = [1,2,4,8]
for num in nums:
    sum = sum+ num
l = len(nums)
ave = sum/l
print(l)
print(sum)
print(ave)

sum = 0
nums =list(range(1,51))
for num in nums:
    sum = sum + num
l = len(nums)
ave = sum / l
print(num)
print(l)
print(ave)

sum = 0
nums = [67,81,92,10,38,45]
a = len(nums)
for num in nums:
    sum = sum + num
ave = sum /a
print(ave)

#累乘-初始值需要赋值为1
a=1
nums =[2,3,4,5]
for num in nums:
    a = a*num
print(a)


a = 1
nums = [1,2,3,4,5]
for num in nums:
    a = a*num
print(a)

a=1
nums = list(range(9,11))
for num in nums:
    a = a*num
print(a)

#列表统计次数
count = 0
snacks = ['chips','chocolate','cookie','chocolate','banana']
for snack in snacks:
    if snack == 'chocolate':
        count=count+1
print(count)

count = 0
nums = [1,2,3,2,3,4,2,35,2]
for num in nums:
    if num ==2:
        count = count+1
print(count)

#列表中元素出现的概率
count = 0
list1 = [4,1,2,3,1,6,1,4]
for a in list1:
    if a == 1:
        count=count +1
l = len(list1)
ratio = float(count/l)
print(ratio)

#利用range()函数，求数字8至50（包括50）的和
sum = 0
nums = list(range(8,51))
for num in nums:
    sum= sum+num

print(sum)

#以知列表c=[1,2,1,6,8,42,1]求元素1出现的次数及概率

c=[1,2,1,6,8,42,1]
count =0
for i in c:
    if i ==1:
        count=count+1
l = len(c)
ratio= count/l
print(count)
print(ratio)

#累加连续的数据
sum =0
for i in range(0,10):
    sum =sum+i
print(sum)

sum =0
for i in range(3,11):
    sum =sum+i
print(sum)

#乘法--累积
#计算1～10的乘积
mul = 1
for i in range(1,11):
    mul =mul*i
print(mul)


#交换两个数
a= 1
b= 2
t =a
a = b
b =t
print(a)
print(b)

a = 2
b = 1
if (a>b):
    t =a
    a = b
    b = t
print(a)
print(b)





