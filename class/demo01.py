# 面对对象编程
'''
类属性、实例属性、初始化方法、实例方法、静态方法、类方法。
'''
# 定义一个Student类
class Student:
    native_place = '河南'#类属性
    def __init__(self,name, age):#初始化方法
        self.name = name    #实例属性
        self.age = age      #实例属性

    #实例方法
    def info(self):
        print('我的名字是:{}，年龄为:{}'.format(self.name, self.age))
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰。')

    #静态方法
    @staticmethod
    def method():
        print('我是静态方法因为我使用了staticmethod进行修饰。')

def main():
    stu1 = Student('张三',23)
    stu2 = Student('李四',20)
    stu1.info()
    stu2.info()
    stu1.age=stu1.age+1
    stu1.info()
    print('学生{}信息的存储地址为:{}'.format(stu1.name,hex(id(stu1))))
    print(stu1)
    Student.native_place='郑州'
    print(stu1.native_place)
if __name__ == '__main__':
    main()
