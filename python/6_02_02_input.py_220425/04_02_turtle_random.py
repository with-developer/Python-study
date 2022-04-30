import turtle
import random


swidth, sheight, pSize = 300, 300, 3
r, g, b, angle, dist = 0, 0, 0, 0, 0
exitCount = 0
curX, xurY = 0, 0
#전역 변수 선언


turtle.title('거북이야 나가지마')
turtle.shape('turtle')
turtle.bgcolor('lightblue')
turtle.pensize(pSize)
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)
#헤더 설정


while True :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))
    angle = random.randrange(0,360)
    dist = random.randrange(100,200)
    turtle.left(angle)
    turtle.forward(dist)

    curX = turtle.xcor()
    curY = turtle.ycor()
    print("X좌표: %.5f, Y좌표: %.5f"% (curX, curY))

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
           pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        exitCount += 1
        print("%d번째 나갔습니다."% exitCount)
        if exitCount >= 3:
            break
    
turtle.done()
