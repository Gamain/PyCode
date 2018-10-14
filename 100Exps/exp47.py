#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：两个变量值互换。
'''

def swap(x,y):
    x,y=y,x
    return (x,y)

x=10
y=20

print swap(x,y)

print "x:",x
print "y:",y
