#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：求一个3*3矩阵主对角线元素之和。
'''
m=[[1,2,3],[4,5,6],[7,8,9]]
print m

s=0
for x in xrange(0,3):
    s+=m[x][x]
print s