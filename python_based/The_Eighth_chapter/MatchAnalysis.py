import random
# 用户体验
def printInfo():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')

def getInputs():
    while True:
        try:
            A = eval(input('请输入选手A的能力值(0-1):'))
            B = eval(input('请输入选手B的能力值(0-1):'))
            N = eval(input('模拟比赛的场次:'))
            return A, B, N
        except:
            print('输入格式错误!!!请重新输入!!!')

def ganmeOver(A_grade,B_grade):
    return A_grade==15 or B_grade==15

def simOneGame(A, B):
    A_grade, B_grade = 0, 0
    falg = 'A'
    while not ganmeOver(A_grade, B_grade):
        if falg == 'A':
            if random.random()<A:
               A_grade+=1
            else:
                falg = 'B' 
        else:
            if random.random()<B:
               B_grade+=1
            else:
                falg = 'A' 
    return  A_grade, B_grade  

def simNGames(A, B, N):
    A_win, B_win = 0, 0
    for i in range(N):
        A_grade, B_grade = simOneGame(A, B)
        if A_grade>B_grade:
            A_win+=1
        else:
            B_win+=1
    return A_win, B_win

def printSummary(A_win, B_win, N):
    print('竞技分析开始，共模拟{}场比赛'.format(N))
    print('选手A获胜{}场比赛，占比{:.1f}%'.format(A_win,A_win/N*100))
    print('选手B获胜{}场比赛，占比{:.1f}%'.format(B_win,B_win/N*100))

def main():
    printInfo()
    A, B, N = getInputs()
    A_win, B_win = simNGames(A, B, N)
    printSummary(A_win, B_win, N)

if __name__ == "__main__":
    main()
