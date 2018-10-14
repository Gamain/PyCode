#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
import string

s=raw_input("请输入一个字符串：")

l=m=n=o=0

for c in s:
    if c.isalpha():
        l+=1
    if c.isspace():
        m+=1
    if c.isdigit():
        n+=1
    else:
        o+=1

print l
print m
print n
print o

print dir('c')
