n, s = 10, 100
ls = ['F','f']

def fact(n):
    global s
    for i in range(1, n+1):
        s*=i
    return s

def func(a):
    ls = []
    ls.append(a)
    return ls

def main():
    func('a')
    print(ls)


if __name__ == '__main__':
    main()