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

uid=1765565108
b =uid%25
print(b)