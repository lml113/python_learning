# object类

class Student(object):

    def __str__(self):
        return '我重写了__str__方法!'


stu =Student()
print(dir(stu))
print(stu)      #默认调用object中的__str__
print(stu.__str__())