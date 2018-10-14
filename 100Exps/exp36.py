#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：求100之内的素数。
'''

s=0
for i in xrange(2,101):
    for j in xrange(2,i):
        if i%j==0:
            break
    else:
        s+=i

print s