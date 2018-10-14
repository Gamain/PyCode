#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：模仿静态变量的用法。
'''

def fun():
    var =0
    var+=1
    print "var:",var

fun()
fun()
fun()

class cls:
    svar=0
    def fun(self):
        cls.svar+=1
        print cls.svar

cs=cls()
cs.fun()
cs.fun()
cs.fun()
print cls.svar