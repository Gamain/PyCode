import types

def fun():
    pass

print (type(fun)==types.FunctionType)
print (type(abs)==types.BuiltinFunctionType)
print (type(lambda x: x)==types.LambdaType)
print (type((x for x in range(10)))==types.GeneratorType)

print (dir(types))