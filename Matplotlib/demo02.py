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

new_ticks = np.linspace(-2*np.pi,2*np.pi,9)
print(new_ticks)
plt.xticks(new_ticks,['-2π', '-1.5π', '-π', '-0.5π', '0','0.5π','π','1.5π','2π'])
plt.yticks([-1,-0.5,0,0.5,1],[r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$very\ good$'])

plt.title('test01')
plt.show()