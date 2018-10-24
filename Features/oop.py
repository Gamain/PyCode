class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def print_score(self):
         print("%s: %s" % (self.__name, self.__score))

sa=Student("Tom",89)
sa.print_score()

sa.__score=99
print(sa.__score)

sa.print_score()