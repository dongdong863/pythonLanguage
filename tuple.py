#!/usr/bin/python
#coding:utf-8

#列表的标志符号是方括号，元祖是小括号
tuples = 'x','y','z'
print(type(tuples))

#只有一个元素的元组
tuples =(1,2,3)

tuples1 =()
print(type(tuples1))
tuples2 =(123)
print(type(tuples2))


#元组拼接
tup1 = ('apple','banana','orage')
tup2 = ('1','2','3')
tup3 = tup1 + tup2
print(tup3)

#删除元组后，不存在
# tup4 = (1,2,3)
# del tup4
# print(tup4)

#len()获取元组长度
tup5 = (1,2,3)
l = len(tup5)
print(l)

#遍历元组
tup6 = ('apple','banana','orange','mango','kiwi')
for i in tup6:
    print(i)
#2*(4)&(4,)*2的区别
print(2*(4))
print((4,)*2)

