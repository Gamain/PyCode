#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
s=int(raw_input("input:"))
m=str(s)

print len(m)

for i in range(len(m)-1,-1,-1):
    print m[i],' ',