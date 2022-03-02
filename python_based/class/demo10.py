# 特殊方法

a = 20
b = 100
c = a+b
d = a.__add__(b)

print(c,'\n',d)


class Student(object):
    def __init__(self,name):
        self.name = name
    def __add__(self,other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')
print(stu1+stu2)    # 实现了两个对象的加法运算（因为在Student类中 编写__add__()特殊方法；
stu = stu1.__add__(stu2)
print(stu)

print('----------------------')
lst = [1,2,3,4,5,6]
print(len(lst))
print(lst.__len__())

print(stu1.__len__())