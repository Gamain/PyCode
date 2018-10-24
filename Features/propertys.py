class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        self.__score=value

sa=Student('Tom',34)

sa.score=90

print(sa.score)

