'''
legend 图例
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y2 = x**2
y1 = 2*x+1
l1,=plt.plot(x,y2,label="2x+1")
l2,=plt.plot(x,y1,color = 'red',linewidth = 1.0,linestyle = '--',label = 'x^2')

#设置边界
plt.xlim(-1,1)
plt.ylim(-1,2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#图标
# plt.legend(loc='upper left')
plt.legend(handles=[l1,l2], labels=['aaa','bbb'], loc='best')


plt.show()