#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''
from math import sqrt

def isPrime(n):
    m=int(sqrt(n))
    for i in range(2,m):
        if(n%i==0):
            return False
    return True

for i in range(101,201):
    if(isPrime(i)):
        print i