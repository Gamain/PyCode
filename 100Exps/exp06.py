#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：斐波那契数列。
'''

# 使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print fib(10)

# 不使用递归
def fibN(n):
    l=[]
    for i in range(1,n):
        if(i<=2):
            l.append(i)
        else:    
            l.append(l[i-2]+l[i-3])
    return l
    
print fibN(10)