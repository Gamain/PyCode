def generator_example():
    yield 1
    yield 2

g=generator_example()
print g,type(g)

for x in g:
    print x
    
print '-------------------'
m=[x*x for x in generator_example() if x>1]
n=(x*x for x in generator_example() if x>1)

print type(m),type(n)

print '-------------------'
for x in m[:]:
    print x
for x in n:
    print x