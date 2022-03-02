'''
封装、继承、方法重写、object类、多态、特殊方法和特殊属性。
面对对象的三大特征
1、封装：提高程序的安全性。
2、继承：提高代码的复用性。
3、多态：提高代码的可扩展性和可维持性。

'''
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand+'汽车已启动...')

a = ['宝马X5','奔驰','大众']

car_n=[]
for item in a:
    car_n.append(Car(item))

print(car_n)

for c in car_n:
    c.start()