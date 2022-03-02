# __new__()与__init__()演示创建对象的过程
'''

'''
class Person:
    def __new__(cls,*args,**kwargs):
        print('__new__(被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id值为：{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__()被调用了，self的id值为：{0}'.format(id(self)))
        self.__name = name
        self.__age = age

print("object类对象的id为：{}".format(id(object)))
print("Person类对象的id为：{}".format(id(Person)))

# 创建Person的实例对象
p = Person('张三',30)
print("p类对象的id为：{}".format(id(p)))