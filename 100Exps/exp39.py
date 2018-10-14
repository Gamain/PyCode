#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''
l=[1,2,3,4,6,7,8,9]
s= int(raw_input("input:"))

for i in xrange(0,len(l)-1):
    if l[i]>s and l[i+1]>s:
        continue
    if l[i]<s and l[i+1]<s:
        continue 
    l.insert(i+1,s)
    break
else:
    if l[-1]>l[0]:          #升序
        if s>l[-1]:
            l.append(s)
        else:
            l.insert(0,s)
    else:                   #降序
        if s<l[-1]:
            l.append(s)
        else:
            l.insert(0,s)
print l