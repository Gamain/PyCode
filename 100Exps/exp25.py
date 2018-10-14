#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：求1+2!+3!+...+20!的和。
'''

n=1
s=0
for i in xrange(1,21):
    n=n*i
    s+=n
print '1! + 2! + 3! + ... + 20! = %d' % s