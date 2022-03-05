'''
Animation动画
'''
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig = plt.figure()
ax1 = plt.subplot(1,2,1)
#fig, ax1 = plt.subplots()

x = np.linspace(0,2*np.pi,600)
line, = ax1.plot(x,np.sin(x))

left, bottom,width,height = 0.6,0.4,0.25,0.25
fig.add_axes([left, bottom,width,height])
line1, = plt.plot(x,np.cos(x))

def animat(i):
    line.set_ydata(np.sin(x+i/10))
    line1.set_ydata(np.cos(x+i/10))
    return line,line1,
def init():
    line.set_ydata(np.sin(x))
    line1.set_ydata(np.cos(x))
    return line,line1,

ani = animation.FuncAnimation(fig=fig,func=animat,frames=600,init_func=init,interval=100,blit=False)


plt.show()
