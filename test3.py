#!/usr/bin/python
#coding:utf-8

# num = int(input('请输入1到100之间的数：'))
# if num >=1:
#     print('在范围内')
# elif num>100:
#     print('在范围外')
# else:
#     print('在范围外')

num=list(range(1,101))
for i in num:
    if i%2!=0:
        print(i)

year = int(input('输入年份：'))
if year %4==0 and year %100!=0:
    print('这个年份是闰年')
else:
    print('这个年份非闰年')