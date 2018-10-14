#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
'''
原理： 给定任意一个整数，从1开始第一个能整除这个整数的数字一定是一个素数
'''
def reduceNum(n):
    while (n!=1):
        for i in range(2,n+1):
            if n % i == 0:
                n /= i # n 等于 n/index
                if n == 1: 
                    print i 
                else : # index 一定是素数
                    print '{} *'.format(i),
                break
            
reduceNum(90)