# 要点： 如果for元素被迭代完，则不会执行else子句  否则会执行else子句
l=[1,2,3,4,5]

for i in l:
    print 'Yes',i
else:
    print 'No'

print '-------------'
for i in l:
    print 'Yes',i
    break
else:
    print 'No'

print '-------------'
for i in l:
    print 'Yes',i
    continue
else:
    print 'No'


print '-------------'
for i in l:
    print 'Yes',i
    if i>10:
        break
else:
    print 'No'

print '-------------'
for i in l:
    print 'Yes',i
    if i>4:
        break
else:
    print 'No'