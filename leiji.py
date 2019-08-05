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



