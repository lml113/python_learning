'''
annotate 标注
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y = 2*x+1
plt.figure(num = 1,figsize=(8,5))

plt.plot(x,y,label="2x+1",color = 'red',linewidth=2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlim(-6,6)
plt.ylim(-6,6)

nx = np.linspace(-6,6,13)
plt.xticks(nx)
plt.yticks(nx)

plt.legend(loc='upper left')

# 添加标注
x0 = 1
y0 = 2*x0+1
# plt.scatter(x0, y0)散点
plt.scatter(x0, y0, s = 50, color = 'black')
plt.plot([x0,x0],[y0,0],'k--',linewidth = 2.5)

# method 1      标注
##########################
plt.annotate('2x+1={0}'.format(y0),xy = (x0,y0),xycoords='data',xytext =(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# method 2
##########################
plt.text(-6,3,r'$This\ is\ the\ some\ text.\ \mu_1\ \sigma_i\ \alpha_t$',
        fontdict={'size':12,'color':'red'})
plt.show()
