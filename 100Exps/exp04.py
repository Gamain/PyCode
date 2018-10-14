#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
leapMonths=(0,31,60,91,121,152,182,213,244,274,305,335)


def isLeapYear(year):
    if(year%100==0):
        return year%400==0
    else:
        return year%4==0

if(isLeapYear(year)):
    print leapMonths[month-1]+day
else:
    print months[month-1]+day
