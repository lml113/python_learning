#蒙特卡罗方法计算圆周率π
import time
import random
N = 1000*1000
n = 0
start = time.perf_counter()
for i in range(N):
    x,y = random.random(),random.random()
    if pow(x**2+y**2,1/2)<1.0:
        n+=1
pi = n/N*4
end = time.perf_counter()-start
print('圆周率为：{0}，计算时间为：{1:.4f}s'.format(pi,end))
