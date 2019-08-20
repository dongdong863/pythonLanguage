#!/usr/bin/python
#coding:utf-8
#常用的python标准库
#第一方面，就是
# python可以随着标准库的使用，，功能增强，比如数学运算的库random提供生成的随机数
# math提供的数学常数和函数，比如派等等
# datetime模块为日期和时间处理提供了方法
# 通过标准库中的re模块，python可以用正则表达式来处理字符窜
# 第二方面，与操作系统，文件系统有关
# 比如sys和os模块
# os提供了很多与操作系统有关的函数
# os模块可以实现操作协同的许多功能，比如管理系统进程，改变当前路径等
# sys模块则被用于管理python自身的运行环境，如判断文件和文件是否存在，获取系统版本之类的操作
# 第三方面，用于访问互联网以及处理网络通信协议的标准库
# 比如socket库
# socket是进程间的一种通信方式，可以实现不同主机间的传输

# 提供派常数的标准库是哪个--math

#正则表达式主要是从字符窜中通过特定的模式搜索想要的内容
#字符窜知识
st=dir(str)
print(st)

#capitalize()作用是把字符窜第一个字符改成大写
str1 = 'i love python'
s=str1.capitalize()
print(s)

#casefold()则是把整个字符窜的所有字符改成小写
str3 = 'I Love Python'
s2 = str3.casefold()
print(s2)


#title()把每隔单词开头第一个字母变成大写
str2 = 'CHeng Xu YUan'
s3 = str2.title()
print(s3)

#find(sub)用来查找sub是否包含在字符窜中，如果包含在字符窜中，返回索引值
s1 = 'i love python'
n = s1.find('o')
print(n)

#返回-1代表不再字符窜中
n1 = s1.find('x')
print(n1)

#join(sub)以字符窜作为分隔符，插入到sub中所有的字符之间---join()中的参数sub是字符窜，被str1隔开了

s1= 'love'
n = s1.join('123456')
print(n)

#lstrip()可以前掉字符窜左边的所有空格
#rstrip()可以删除字符窜末尾的空格
#rfind（）从右边开始查找
#split()不带参数，默认是以空格为分隔切片字符窜
#split()带参数，就是以参数为分隔切片字符窜
#translate()和str.maketrans()把字符窜中的字符换成别的字符

s = 'xxxxxaaaaaxxxx'
n=s.translate(str.maketrans('x','b'))
print(n)


#format字符窜格式化
#比如常会输出，'xxx，你xx月话费是xxxx'之类的字符窜--xxx的内容是根据变量变化的，所以要一种格式化字符窜的方式
#麻烦的写法
a='{0} love {1}'.format('I','Python')
print(a)

#格式话操作符来实现格式化
# %s格式化字符窜
# %d格式化整数
# %f格式化浮点数
# %c格式化字符机器ASCII码
# %o格式化八进制
# %x格式化十六进制
# %e科学计数法格式化浮点数
# %g根据值的大小决定使用%f或者%e

#%s的用法
#单个%s，通过"%s" % "替换%s的真是值"的格式

a ="%s" % "I love python"
print(a)

#duoge %s
a = "%s love %s" %("i","python")
b = "%s %s %s yeah"%("i","love","python")
print(a)
print(b)

#%d的用法
#单个%d
age = "i am %d years old" %20
print(age)
#多个%d
num = "%d+%d=%d" %(1,2,3)
print(num)

#%f
#单个%f,默认精确到6位小数，用0补充
f = "%f" % 2.3
print(f)

#浮点数可以指定整数与小数的位数
m = "%1f"%2.35
print(f)
e = "%5.1f"%2.88#5是总的位数，在2前面用空格补
print(e)


#用0在前面填补
e = "%05d"%6#5是总位数，0是在数字前面补0凑够5位数
print(e)

#+、-是在前面补还是后面补
e ="%-5d"%6
print(e)

e = "%+5d"%8
print(e)

#正则表达式 regular expression
#判断字符窜是否正确的电话号码或者邮箱等，使用字符窜的方法就很复杂
#re模块可以使用正则，指定一些规则来描述你希望匹配的字符窜集合
#[0-9]意思是从字符中找一个0到9的数字字符，group()查看匹配结果
import re
m = re.search('[0-9]','abc3cdef')
# n = re.search('[0-3]','abcdsef')#匹配不到结果返回NoneType类型
print(m.group())
# print(n.group())

#\d与[0,9]作用一样
m = re.search('\d','abc3def')
print(m)

#\w可以匹配一个数字或者字母
#00\d只能匹配到007不能匹配到00a
#00\w可以匹配到007，也能匹配到00a
m = re.search('00\w','abc003nn00a.txt')
print(m.group())

#.可以匹配除换行符\n之外的任何字符
#所以.可以匹配数字、字母、符号等等字符
m = re.search('n.','python!')
print(m.group())

#匹配变长的字符，可以用{n}表示n个字符
#用{n,m}表示n到m个字符这样一个范围，优先匹配m个，最少匹配n个
# m = re.search('a{2,6}','abcdefghijk')
# print(m.group())

#\s  可以匹配任何空白字符（包含空格、换行符等）
m = re.search('\d\s','001 ae2')
print(m.group())

#+表示至少一个字符、？表示0个或者1个字符

#[]比如[0-9a-zA-Z]可以匹配一个数字或者字母
m =re.search('[0-9a-zA-Z]','b_3_afi')
print(m.group())

#[0-9a-zA-Z]+就是表示可以匹配至少一个数字或者字符组成的字符窜
m = re.search('[0-9a-zA-Z]+','!_a3fi')
print(m.group())

#A|B可以匹配A或者B
m = re.search('(P|p)ython','Python')
print(m.group())

#^表示行的开头，^\d表示必须以数字开头
#$表示一行的结束，\d$表示必须以数字结束

m = re.search('^\d','3a,python')
n = re.search('\d$','3ab4,uuui1')
print(m.group())
print(n.group())


#^python$,'python'就成了整行匹配了
#^py$,'python'---none变成恶整行匹配，只能匹配py

#search()遍历字符窜，找到正则表达式匹配的第一个位置
#math()则判断一个正则表达式是否从开始处于匹配一个字符窜

#findall()返回所有匹配结果，返回的是一个列表
#返回结果是字符窜中所有数字字符构成的列表
m = re.findall('\d','我有1个苹果，2个梨和3个桃子')
print(m)

m = re.search('[a-zA-Z0-9]{2,4}','x.5h3Wng')
print(m.group())

#*标识任意个字符（包括0个）
m =re.search('ca*t','ct')
n = re.search('ca*t','caat')
b = re.search('ca*t','caaaaat')

print(m.group())
print(n.group())
print(b.group())

#具有其他的含义的字符叫元字符
#^,$,*,+,?,{},[],|,(),\
#元字符在方括号仲不表示特殊含义
#$是一个元字符，在[]中只匹配$字符本身

m = re.search('[a-z$]','abced123')
print(m.group())

#python的字符窜本身用反斜杠\转义
#比如字母n前面加上\，那么\n就表示换行
x = 'abc\nabc'
y = 'abc\\n'
print(x)
print(y)
#一般使用python的原始字符窜r
a = r'abc\n'
print(a)

#正则表达式里通常包含反斜杠，想\s都有特殊含义
#匹配的字符窜是'\s',正则表达式就要写成r'\\s'
#pythonde r前缀，就不用考虑转义的问题
m = re.search(r'\\s','\s')
print(m.group())

#匹配至少一个数字
#compile()用于编译正则表达式
#\d+至少一个是数字
#match从第一个开始匹配，不对的返回none
p = re.compile(r'\d+')
m = p.match('1abcd123456bb')
print(m.group())

#用match()指定匹配开始和结束的位置
p = re.compile(r'\d+')
m = p.match('abc123bbbb',3,5)#第4位开始第6位结束
print(m.group())

#提取子窜---用group(x)提取分组
#先定义两个组
p = re.compile(r'(^\d{3})-(\d{3,8}$)')
m = p.match('021-123456')
print(m.group())
#返回第一个分组匹配成功的子窜
print(m.group(1))
#返回第二个分组匹配成功的子窜
print(m.group(2))
#返回所有分组内容，相当于(m.group(1),m.group(2),......)
print(m.groups())
#第三个分组不存在
# print(m.group(3))

p = re.compile(r'([a-zA-Z]+) ([a-zA-Z]+)')
m = p.match('Hello Cheng Xu Yuan')
print(m.group())

#切分字符窜
#re.split()是按照能够匹配的子窜将字符窜分割后返回列表
a='a b   c'.split()
print(a)

p = re.split(r'\s+','a b  c')
print(p)
#包含逗号
# p = re.split(r'[\s,]+','a,b,  c')
# print(p)

#正则表达式是贪婪匹配,\d+把后面的1全部匹配了，1*值只有匹配空字符窜了
p = re.compile(r'(\d+)(1*)')
m = p.match('22111111')
print(m.groups())

p = re.compile(r'(\d+?)(1*)$')
m = p.match('2233111111')
print(m.groups())