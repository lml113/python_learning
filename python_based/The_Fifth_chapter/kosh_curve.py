# 科赫曲线绘制
# 科赫雪花绘制
import turtle

def koch(n,size):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(n-1,size/3)


turtle.setup(600,600)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.pensize(2)
for i in range(3):
    koch(3,400)
    turtle.right(120)
turtle.hideturtle() #海龟隐藏
turtle.done()
