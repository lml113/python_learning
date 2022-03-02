import time

t = time.gmtime()
t1 = time.strftime("%Y-%m-%d %p %H:%M:%S",t)
print(type(t1))
print(t1)