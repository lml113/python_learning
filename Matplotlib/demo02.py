'''

设置坐标轴1

'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi,1000)
y = np.cos(x)
plt.figure()
plt.plot(x, y)
plt.xlim(-2*np.pi, 2*np.pi)
plt.xlabel("I am x")
plt.ylim(-1,1)
plt.ylabel('I am y')

plt.title('test01')
plt.show()