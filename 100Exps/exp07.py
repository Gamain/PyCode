#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：将一个列表的数据复制到另一个列表中。
'''

m=[1,2,5,'ABC']
n=[]

for i in m[:]:
    n.append(i)
print(n)