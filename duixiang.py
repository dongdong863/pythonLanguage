#!/usr/bin/python
#coding:utf-8

# #对象=属性+方法
# class student:
#     age =23
#
# #创建对象，object = class()
# #对象.属性用来引用属性
#
# p1= student()
#
# print(p1.age)

#如果类中定义了__init__()这个方法，创建对象时，python会自动调用这个方法，这个过程叫初始化
#定义方法的时候，必须又self这一个参数，这个参数表示某个对象
#a1在类中就是作为self来作用的
# class Animals:
#     age = 5
#
#     def __init__(self,name):
#         self.name = name
#         print(self.name)
#
# a1 = Animals('dog')
# a2 = Animals('cat')


#属性的操作
class Student:
    '帮助信息：xxxxx'
    age=13
    def __init__(self,name):
        self.name = name
        print('你的名字：'+name)
    def show(self):
        print(self.age)
p1 = Student('小明')
p2 = Student('小白')

print(p1.name)
p1.show()
p1.name = '小红'
print(p1.name)
#删除对象的属性，
#1、 del 对象.属性

# del p1.name
# print(p1.name)
#2、hasattr()--确认,确认对象的属性，返回True说明p1有这个属性
print(hasattr(p1,'name'))

#getattr()获取对象的属性
print(getattr(p1,'name'))

#setattr()改变对象属性的值
setattr(p1,'name','小黄')
print(getattr(p1,'name'))

#delattr()删除对象属性的值

#查看帮助信息---类.__doc__
print(Student.__doc__)

#查看类的名字
print(Student.__name__)

#类的父类构成的元素
print(Student.__bases__)


#动物是父类，猫狗等等是子类
class Parent:
    def p(self):
        print("这个是父类的方法")
#继承父类，就需要在子类名称后的括号写上父类的名称，子类(父类)
class Child(Parent):
    def c(self):
        print("这个是子类的方法")
#创建子类的一个对象片p1就自动有父类的属性
#p1包含了父类Parent的方法p()
p1 = Child()
p1.p()


#object的含义，出现obiect时说明没有父类了
class Parent(object):
    def p(self):
        print("这个是父类的方法")
class Child(Parent):
    def c(self):
        print("这个是子类的方法")
p1 = Child()
p1.p()

#子类定义的方法或者属性跟父类同名时，子类的会覆盖父类的

class A:
    def Hello(self):
        print("父类的hello")
class B(A):
    def Hello(self):
        print("子类的Hello")
a1 = B()
a1.Hello()


#父类方法跟子类方法同名时，父类的方法没有变
class C(object):
    def Hello(self):
        print("父类的hello")
class D(Parent):
    def Hello(self):
        print("子类的Hello")
c1 = C()
c1.Hello()
d1 = D()
d1.Hello()


#定义一个类叫动物，动物下有一个类叫狗，没有属性和方法写pass
#pass是个空语句，不做任何事情，为了保持程序结构的完整性
class Animal(object):
    pass
class Dog(Animal):
    pass

#在Dog类中用__init__()定义狗的名字吧
class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.name = name
        print(self.name)

#在上面的基础上，创建狗的对象，分别命名为吉娃娃，哈士奇，泰迪
d1 = Dog('吉娃娃')
d2 = Dog('哈士奇')
d3 = Dog('泰迪')


#定义一个类叫动物，动物下还有一个类叫鱼，鱼里面又有金鱼，鲨鱼，鲤鱼

class Animal(object):
    pass
class Fish(Animal):
    def __init__(self,name):
        self.name = name
        print(self.name)
f1 = Fish('金鱼')
f2 = Fish('鲨鱼')
f3 = Fish('鲤鱼')