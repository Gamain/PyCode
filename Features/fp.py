#!/usr/bin/python
# -*- coding: utf-8 -*-

def add(x, y, f):
    return f(x)+f(y)


def func(a):
    return a*a


print add(2, 3, func)

print map(func, [1, 2, 3, 4, 5])


def foo(a, b):
    return a+b


print reduce(foo, [1, 2, 3, 4, 5])


def bar(a, b):
    return a-b


print reduce(bar, [0, 1, 2, 3, 4, 5])


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print "3"


def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x*y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def is_odd(n):
    return n % 2 == 1

print list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
 
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        #print(n)
        break
    else:
        break


print '----------------------'

def lazy_add(*args):
    def sum():
        ax=0
        for i in args:
            ax+=i
        return ax
    return sum

f=lazy_add(1,2,3,4,5)
print f()

print '========================='

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

fs= count()
print fs[0]()
print fs[1]()
print fs[2]()

print '========================='

def count2():
    fs = []
    #def fx(x):
    #   def fy():
    #       return x*x
    #   return fy

    def fx(x):
        return lambda:x*x
        
    #这个语法貌似不支持 不知道py3十分支持
    #fz=lambda x :(lambda:x*x)

    for i in range(1, 4):
        fs.append(fx(i))
    return fs

fs2= count2()
print fs2[0]()
print fs2[1]()
print fs2[2]()