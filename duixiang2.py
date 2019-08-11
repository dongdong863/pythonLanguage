#!/usr/bin/python
#coding:utf-8

#圆形面积是半径的平方乘派，乘方符号是**，我们的派值简略为3.14
class Circle(object):
    pi=3.14
    def __init__(self,r):
        self.rad = r
    def area(self):
        a = self.pi*self.r**2
        return a
