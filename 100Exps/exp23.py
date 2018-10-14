#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''
import math

for i in xrange(0,7):
    m=int(math.fabs(3-i))
    n=7-2*m
    for j in xrange(1,m+1):
        print ' ',
    for j in xrange(1,n+1):
        print '*',
    for j in xrange(1,m+1):
        print ' ',
    print ''