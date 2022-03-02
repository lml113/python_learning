#动态绑定属性与方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # 实例方法
    def eat(self):
        print(self.name+'在吃饭')

def show():
    print('我是一个函数')
    
stu1 = Student('张三',20)
stu2 = Student('李四',30)
stu1.genter = '女'  #动态绑定属性
stu1.eat()
stu2.eat()
print(stu1.name,stu1.age,stu1.genter)
print(stu2.name,stu2.age)
stu1.show = show    # 动态绑定方法
stu1.show()