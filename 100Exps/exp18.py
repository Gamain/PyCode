#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。。
'''
a=int(raw_input("a:"))
n=int(raw_input("n:"))

l=[0]
for i in xrange(1,n+1):
    l.append(l[i-1]*10+a)
print(l)
s=0
for i in l[:]:
    s+=i
print s