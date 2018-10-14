#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：暂停一秒输出。
'''
import time

print  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
time.sleep(2)
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))