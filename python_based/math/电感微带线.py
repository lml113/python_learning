from cmath import pi, tan
import numpy as np
import math
L = 1e-8
# 默认参数
H = 0.508e-3
er = 3.66
w = 2*np.pi*2000000000
Z0=50
a = np.arctan(w*L/Z0/360*2*np.pi)
l = a/er
print(a)
print(l)