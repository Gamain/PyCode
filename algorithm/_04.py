'''
题目：把字符串中的空格替换成'20%'

方法1：直接使用Python字符串的内置函数
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        l=[]
        i=0
        while i<len(s):
            if s[i]==' ':
                l.append('%20')
            else:
                l.append(s[i])
            i+=1
        return ''.join(l)

s='Are you Ok?'
slu=Solution()

print (slu.replaceSpace(s))

assert slu.replaceSpace(s)=='Are%20you%20Ok?'