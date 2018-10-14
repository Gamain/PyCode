#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

s=raw_input("string:")

def prt(s):
    if(len(s)==0):
        return
    c=s[-1]
    print c,
    s=s[0:len(s)-1]
    prt(s)

prt(s)