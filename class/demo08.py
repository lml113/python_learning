# 多态的实现
'''
简单地说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，
仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
'''
class Animals(object):
    def eat(self):
        print('动物会吃')

class Dog(Animals):
    def eat(self):
        print('狗吃骨头...')

class Cat(Animals):
    def eat(self):
        print('猫吃鱼...')

class Person():
    def eat(self):
        print('人吃五谷...')

# 定义一个函数
def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animals())

print('........................')
fun(Person())