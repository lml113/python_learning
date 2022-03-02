# 七段数码管绘制
# 导入模块
from tkinter import Y
import turtle as t
import random
import time


#划一条40像素的直线
def drawLine(draw):
    #自动随机生成RGB值
    color_1,color_2,color_3 = random.randint(0,25),random.randint(0,25),random.randint(0,25)
    t.pencolor(color_1*10,color_2*10,color_3*10) #定义画笔颜色
    t.pendown() if draw else t.penup()
    t.fd(20)
    t.right(90)

#根据输入数字，起始坐标（默认(0,0)），画一位数码管
def drawdigital(digital,startx=0,starty=0):
    t.colormode(255)    #设置RGB为0~255
    t.speed(0)          #定义速度
    t.pensize(4)       #定义画笔粗细
    t.penup()
    t.goto(startx,starty)
    t.pendown()
    drawLine(True) if digital in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digital in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digital in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digital in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digital in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digital in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digital in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)

def draw_dot(x,y):
    color_1,color_2,color_3 = random.randint(0,25),random.randint(0,25),random.randint(0,25)
    t.pencolor(color_1*10,color_2*10,color_3*10) #定义画笔颜色
    #t.pensize(2)       #定义画笔粗细
    for i in [-10,10]:
        t.penup()
        t.goto(x+10,y+i)
        t.pendown()
        t.dot()


#main函数
def main():
    t.Turtle().screen.delay(0)
    tm = time.strftime("%H-%M-%S-%Y-%m-%d",time.localtime()).split('-')
    H = int(tm[0])
    M = int(tm[1])
    S = int(tm[2])

    Y = int(tm[3])
    m = int(tm[4])
    d = int(tm[5])
    t.setup(350,200)
    drawdigital(Y//1000,-130,40)
    drawdigital(Y//100%10,-100,40)
    drawdigital(Y//10%10,-70,40)
    drawdigital(Y%10,-40,40)
    draw_dot(-15,40)
    drawdigital(m//10,10,40)
    drawdigital(m%10,40,40)
    draw_dot(65,40)
    drawdigital(d//10,90,40)
    drawdigital(d%10,120,40)

    drawdigital(H//10,-105,-40)
    drawdigital(H%10,-75,-40)
    draw_dot(-50,-40)
    drawdigital(M//10,-25,-40)
    drawdigital(M%10,5,-40)
    draw_dot(30,-40)
    drawdigital(S//10,55,-40)
    drawdigital(S%10,85,-40)
    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()