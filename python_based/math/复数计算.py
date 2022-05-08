import numpy as np
a = complex(0.31*np.cos(100/360*2*np.pi),0.31*np.sin(100/360*2*np.pi))
print(a)
z = (1+a)*50/(1-a)
print(z)