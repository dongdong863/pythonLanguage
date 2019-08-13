#!/usr/bin/python
#coding:utf-8
#单个模块测试
def cal(x,y):
    m= x+y
    return m

def test():
    print("模块测试结果：",cal(3,4))

#在主程序中调用name就会是'__main__'
#在模块中调用name么么就会是模块的名字
print(type(__name__))
print(__name__)

if __name__ == '__main__':
    test()
