#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocess import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q,l):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C','D']:
        print('Put %s to queue...' % value)
        q.put(value)
        l.append(value)
        print l
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q,l):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
        print l

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    l=[]
    pw = Process(target=write, args=(q,l))
    pr = Process(target=read, args=(q,l))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()