import time

t = time.time()
print('{:,.4f}'.format(t))

t_t = time.ctime()
print(type(t_t),t_t)

t2 = time.gmtime()
print(type(t2))
print(t2)