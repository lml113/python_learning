# 阶乘
#函数定义
# 计算n的阶乘，返回n值与m值。
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m,n,m
#   main函数
def main():
    n = 10
    result = fact(n)
    print(type(result),result)
    result_list = list(result)
    print(type(result_list),result_list)


if __name__ == '__main__':
    main()