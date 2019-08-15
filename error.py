#!/usr/bin/python
#coding:utf-8
#语法错误：漏打符号或者编写程序错误
#异常Exception：语句或者表达式在语法上是正确的，但是执行是可能会导致错误，比如字段只有3个键，取第4个，执行时会报错

#TypeError、IndexError、keyError、ZeroDivisionError

#FileNotFoundError找不到文件产生的异常
#文件夹下有read.txt，只输入read，就会报错，python并不知道read文件是说明
# file_name = input("请输入文件名：")
# f = open(file_name)

#多个异常
#处理异常
# try：
#     #检测范围
# except Exception[as reson]:
#     #出现异常后的处理

# f = open('file.txt')
# print(f.read())
# f.close()
#处理异常
# try：
#     #检测范围
# except Exception[as reson]:
#     #出现异常后的处理

# f = open('file.txt')
# print(f.read())
# f.close()
#找不到文件异常
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('文件出错了')

#0 不能做除数异常
try:
    num1=input('请输入被除数：')
    num2=input('请输入除数：')
    result = int(num1)/int(num2)
    print(result)
except ZeroDivisionError:
    print('0不能做除数')

#查看具体出错原因
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError as reason:
    print('出错的原因：'+str(reason))


#找不到文件异常
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('文件出错了')

#0 不能做除数异常
try:
    num1=input('请输入被除数：')
    num2=input('请输入除数：')
    result = int(num1)/int(num2)
    print(result)
except ZeroDivisionError:
    print('0不能做除数')

#查看具体出错原因
try:
    f= open('file.txt')
    print(f.read())
    f.close()
except FileNotFoundError as reason:
    print('出错的原因：'+str(reason))

try:
    sum = 1+'1'
    f = open('file.txt')
    print(f.read())
    f.close()
except (TypeError,FileNotFoundError) as reason:
    print('出错了\n出错的原因是：'+str(reason))

#tyr里面的异常没有在except出现，也会报错
#只要try里有一行代码命中except里的Error，命中的那条代码try里面后面的那些代码都不执行了


#finally
try:
    f = open('file.txt','w')
    f.write('123')
    a=1+'2'
    #f.close()如果放在这里，就不会执行到这句话，文件没有被保存
except (OSError,TypeError) as reason:
    print('出错了\n出错的原因是：'+str(reason))
finally:
    f.close()

#try...except...else
#try语句执行时没有异常，python执行else后的语句

try:
    int('123')
except VauleError as reason:
    print('出错了\n出错的内容是：'+str(reason))
else:
    print('无异常')
