#!/usr/bin/python
# -*- coding: utf-8 -*-

count=0

def foo():
    count=10
    print "from foo:",count
    count+=1

def bar():
    global count
    print "from bar:",count
    count+=1

for x in range(3):
    foo()
    bar()

print "count:",count