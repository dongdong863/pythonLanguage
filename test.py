# -*- coding:utf-8 -*-
saraly = int(input())

if saraly<=500:
    print('欢迎进入史塔克穷人帮前三名')

    if saraly>100:
        print('请找弗瑞队长加薪')

    elif saraly<=100:
        print('恭喜您荣获“美元队长”称号！')

elif saraly>500:
	print('祝贺您至少可以温饱了。')

elif saraly<1000:
    print('经济危机都难不倒您！')

    if saraly<=20000:
        print('您快比钢铁侠有钱了！')

    elif saraly>20000:
        print('您是不是来自于瓦坎达国？')
print('程序结束')