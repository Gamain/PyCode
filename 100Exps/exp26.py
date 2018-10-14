#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：利用递归方法求5!。
'''

def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

print fact(5)