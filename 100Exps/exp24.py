#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

f1=f2=1.0
l=[]
for i in xrange(1,11):
    f1=f1+f2
    print f1,'/',f2
    l.append(f1/f2)
    f2=f1+f2
    print f2,'/',f1
    l.append(f2/f1)
print "sum:",reduce(lambda x,y:x+y,l)