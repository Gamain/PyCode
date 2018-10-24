class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

    def __init__(self,name,age):
        self.name=name
        self.age=age

sa=Student("Tom",27)
sa.Sex=1