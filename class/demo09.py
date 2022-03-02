# 特殊方法和特殊属性
'''
特殊属性
1、__dict__：获得类对象或实例对象所绑定的所有属性和方法的字典
特殊方法
1、__len__()：通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
2、__add__()：通过重写__add__()方法，可以使用自定义对象具有“+”功能。
3、__new__()：用于创建对象。
4、__init__()：对创建的对象进行初始化。

'''

# print(dir(object))  # 查看类的属性与方法

class A:
    def __init__(self,name):
        self.name = name

class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

x = C('张三',25)# x是C类型的一个实例对象
print(x.__dict__)# 实例对象的属性对象
print(C.__dict__)
print('-----------------------')
print(x.__class__)# 输出对象所属的类
print(C.__bases__)# C类的父类类型的元素
print(C.__base__)# 输出第一个C类的父类类型的元素
print(C.__mro__)# 类的层次结构
print(A.__subclasses__())# A的子类类型的元素

