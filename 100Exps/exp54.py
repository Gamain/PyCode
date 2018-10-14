#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：取一个整数a从右端开始的4〜7位。
'''
s=raw_input("input:")

if len(s)<4:
    pass
else:
    if(len(s)<7):
        print s[3:]
    else:
        print s[3:7]