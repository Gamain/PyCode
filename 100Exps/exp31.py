#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
l=["Mondy","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def find(s):
    k=[]
    for x in l[:]:
        fl=True
        for y in  xrange(0,len(s)):
            if x[y]!=s[y]:
                fl=False
                break
        if fl==True:
            k.append(x)
    return k

s=raw_input("please input:")
t=find(s)
while len(t)>1:
    s+=raw_input("please input:")
    t=find(s)
if(len(t)==0):
    print "input error"
else:
    print(t[0])