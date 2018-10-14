#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

for i in xrange(1,1001):
    l=[]
    sum=0
    for j in xrange(1,i):
        if(i%j==0):
            l.append(j)
            sum+=j
    if(sum==i):
        print i
        print l
