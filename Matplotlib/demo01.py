'''

figure 图像

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = x**2
y3 = 2*x**2
plt.figure()
plt.plot(x, y1, 'r')
plt.figure(num = 3,figsize=(8,5))
plt.plot(x, y1, 'r')
plt.plot(x, y2, color = 'black',linewidth = 1.0, linestyle = '--')
plt.plot(x, y3, color = 'blue')
plt.show()