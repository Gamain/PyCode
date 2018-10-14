#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输出 9*9 乘法口诀表。
'''

for i in range(1,10):
    for j in range(1,10):
        if(i<j):
            continue
        print i,"*",j,"=",i*j,
    print "\n"