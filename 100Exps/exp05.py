#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''
l=[]
for i in range(3):
    number=int(raw_input('integer:\n'))
    l.append(number)
l.sort()
print l