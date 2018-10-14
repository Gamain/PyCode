#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
s=100.0
l=[]
for i in xrange(1,12):
    if i==1:
        l.append(s)
    else:
        l.append(2*s)
    s=s/2
print l

print l[10]/2

sum=0
for i in l[:10]:
    sum+=i
print sum
