import turtle
import random

def screenLeftClick (x,y):
    global r, g, b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick (x,y):
    global r, g, b

    turtle.pencolor(r,g,b)
    turtle.penup()
    turtle.goto(x,y)


def screenMidClick (x,y):
    global r, g, b
    tSize = random.randrange(1,10)

    r= random.random()
    g= random.random()
    b= random.random()

    pSize = random.randrange(1,10)
    turtle.pensize(pSize)
    turtle.shapesize(tSize)

pSize = 10
r, g, b = 0.25, 0.25, 0.25

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.bgcolor('lightblue')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)


turtle.done()
