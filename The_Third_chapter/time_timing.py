import time

def wait(n):
    time.sleep(n)

start = time.perf_counter()
i=1000
while(i):
    i-=1
end = time.perf_counter()
t = end-start
print(t,'s')
wait(3.3)
end = time.perf_counter()
t = end-start
print(t,'s')