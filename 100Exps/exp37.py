#!/usr/bin/python
# -*- coding: utf-8 -*-
    
'''
题目：对10个数进行排序。
'''
l=[2,5,5,6,2,8,1,7,90,3]

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]

print l
