#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

while True:
    s=int(raw_input("input:"))
    q=s*s
    print q
    if q<50:
        break
