#!/usr/bin/python
#coding:utf-8
#dict = {key1:value1,key2:value2}
#字典中的键必须是唯一的，值可以不唯一
# 值可以去任何数据类型，但是键必须是不可变的，
# 像字符窜，数字或元组这样不可变的才能是值
# 列表不能作为字典里的键

dict ={'name':'Lily','city':'beijing'}
print(dict['name'])

#字典增加元素
dic ={'name':'Lily','city':'beijing'}
dic ['age']=15
print(dic)


#字典的元素没有顺序，所以不能通过下标引用元素，字典里，键只能出现一次
#同样的键最后一个会覆盖第一个
dict ={'name':'Lily','city':'beijing','name':'bili'}
print(dict['name'])

#修改元素
dict ={'name':'Lily','city':'beijing'}
dict['name']='bili'
print(dict)

#删除元素
dict1 ={'name':'Lily','city':'beijing'}
del dict1['name']
print(dict1)

#清楚整个字典
dict2 ={'name':'Lily','city':'beijing'}
dict2.clear()
print(dict2)

#del和clear字典的区别
#del是删除这个字典，字典不存在了，clear是清空，但是字典还在
# 但是字典还在dict3 ={'name':'Lily','city':'beijing'}
# dict3.clear()
# print(dict3)
# del dict3
# print(dict3)


#历遍字典的键（key）
d = {'list':[1,2,4],'apple':'苹果','tup':(4,5,6),1:789}
for key in d:
    print(key)#在循环中，字典的每个键，被提取出来
print(d.keys())#d.keys()这个方法可以返回字典所有的键


#历遍字典的值
d = {'list':[1,2,4],'apple':'苹果','tup':(4,5,6),1:789}
for v in d.values():#d.values()这个方法是取所有字典里的值
    print(v)

#历遍字典的项
d = {'list':[1,2,4],'apple':'苹果','tup':(4,5,6),1:789}
for i in d.items():
    print(i)
    
    
#历遍字典的键值
d = {'list':[1,2,4],'apple':'苹果','tup':(4,5,6),1:789}
for key,value in d.items():
    print(key,value)
print('--------------分割线----------------')
for (key,value) in d.items():
    print(key,value)
    
#fromkeys()方法，它可以创建并返回新的字典
#d.fromkeys(k,v)这个是fromkeys()方法的使用格式，它会返回一个新的字典
dic9={}
dic9=dic9.fromkeys((1,2,3))#(1,2,3)是字典的键
print(dic9)
dic9 = dic9.fromkeys((1,2,3),'number')#number每个键的值都是'number'
print(dic9)
#这里不会自动匹配，只会把（'one','two','three'）
dic6 = {}
dic6 = dic6.fromkeys((1,2,3),('one','two','three'))
print(dic6)
#重新创建一个字典
dic5 = {}
dic5 = dic5.fromkeys((1,2,3),('one','two','three'))
print(dic5)
dic5 = dic.fromkeys((1,3),'key')
print(dic5)

#in,not in 判断是否在字典中
#键in字典
dic2 = {}
dic2 = dic2.fromkeys(range(5),'number')
print(dic2)
print(0 in dic2)
print(6 not in dic2)
print(6 in dic2)

#弹出指定键的值(弹出后字典里这一项就不存在了)
a = {1:'one',2:'two',3:'three'}
a.pop(2)
print(a)
#随机弹出一个键的值，有的会删最后一个，有时会删第一个
a = {1:'one',2:'two',3:'three'}
print(a)
print(a.popitem())
print(a)

#更新字典内容(b跟新了a)
#更新的项里有原字典的键值，那么元字典中响应的项就会更新，
#如果没有的话，就在原有的字典的末尾添加新的键值
a = {1:'one'}
print(a)
b = {1:'two'}
#b={2:'two'}
a.update(b)
print(a)
