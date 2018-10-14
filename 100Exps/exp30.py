#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
s=int(raw_input("input:"))

if (s/10000==s%10) and (s%10000/1000==s%100/10):
    print True
else:
    print False