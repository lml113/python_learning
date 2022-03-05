'''
次坐标
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x,y1,'g',linestyle = '--')
ax1.set_ylabel('g',color='g')
ax2.plot(x,y2,'r')
ax2.set_ylabel('r',color='r')

plt.show()