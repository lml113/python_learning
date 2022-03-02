# 读取data.txt文件数值，绘制图像
import turtle as t

l_list = []
with open(r'F:\vscode\python\course\The_Seventh_chapter\data.txt','r') as f:
    for line in f:
        line = line.replace('\n','')
        l_list.append(list(map(eval,line.split(','))))
t.setup(800,600)
t.pensize(5)
for i in range(len(l_list)):
    t.pencolor(l_list[i][3],l_list[i][4],l_list[i][5])
    t.fd(l_list[i][0])
    if l_list[i][1] == 1:
        t.right(l_list[i][2])
    else:
        t.left(l_list[i][2])