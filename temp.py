# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1 摄氏度华氏度转换
temp = input("请输入带有符号的温度值：")
if temp[-1] in ['F','f']:
    C = (eval(temp[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
    #print格式化，理解为format(C，.'2f')
elif temp[-1] in ['C','c']:
    F = 1.8*eval(temp[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误。")