from turtle import *
from random import randint

hideturtle()
tracer(0)
speed(999)
penup()
setposition(0,-300)
left(90)
pendown()
thick = 10
pensize(thick)
pencolor('#a3d6c0')

axiom = "A"
axmTemp = ""
itr = 6
angl = 35
dl = 70
stc = []
translate={"A":"i[-A]i[+A]I[-A]I0",
           "0":"1",
           "1":"2",
           "2":"3",
           "3":"4",
           }

for k in range(itr):
    for ch in axiom:
        if ch in translate:
            axmTemp+=translate[ch]
        else:
            axmTemp+=ch
    axiom = axmTemp
    axmTemp = ""

for ch in axiom:
    if ch == "+":
        right(angl - randint(-5,5))

    elif ch == "-":
        left(angl - randint(-5,5))

    elif ch =="i":
        forward(dl/3)

    elif ch == "A":
        forward(dl)
        stc.append(pensize())
        pensize(1)
        pencolor('#000000')
        fillcolor("#79b465")
        setheading(heading()-90)
        startHeading = heading()
        begin_fill ()
        circle(4.5, -160)
        right(60)
        circle(7, -79)
        end_fill ()
        setheading(startHeading)
        begin_fill ()
        circle(4.5, 160)
        left(60)
        circle(7, 79)
        end_fill ()
        pensize(stc.pop())
        pencolor('#a3d6c0')
    
    elif ch == "I":
        forward(dl)

    elif ch == "0" or ch == "1":
        stc.append(pensize())
        pensize(1)
        pencolor('#000000')
        fillcolor("#79b465")
        setheading(heading()-90)
        startHeading = heading()
        begin_fill ()
        circle(4.5, -160)
        right(60)
        circle(7, -79)
        end_fill ()
        setheading(startHeading)
        begin_fill ()
        circle(4.5, 160)
        left(60)
        circle(7, 79)
        end_fill ()
        pensize(stc.pop())
        pencolor('#a3d6c0')

    elif ch == "2" or ch == "3":
        stc.append(pensize())
        fillcolor ("#fc0fc0")
        pencolor('#000000')
        pensize(1)
        begin_fill ()
        for i in range(8):
            for j in range(5):
                right(72)
                forward(6)
            right(45)
        end_fill ()
        pensize(stc.pop())
        pencolor('#a3d6c0')

    elif ch == "4":
        stc.append(pensize())
        pensize(1)
        pencolor('#000000')
        startHader = heading()-90
        setheading(90+startHader)
        fillcolor("#c6cf99")
        begin_fill()
        right(50)
        circle(2*5,45)
        circle(5,180)
        circle(2*5,45)
        circle(0.586*5,90)
        end_fill()
        circle(2*5,45)
        circle(5, 130)
        begin_fill()
        circle(-5, 90)
        right(100)
        circle(-10, 60)
        end_fill()
        left(180)
        begin_fill()
        circle(-5, 90)
        right(100)
        circle(-10, 50)
        end_fill()
        left(110)
        begin_fill()
        circle(5, 90)
        left(100)
        circle(10, 50)
        end_fill()
        pensize(stc.pop())
        pencolor('#a3d6c0')

    elif ch == "[":
        thick = thick*0.75
        dl = dl*0.8
        pensize(thick)
        stc.append(thick)
        stc.append(dl)
        stc.append(xcor())
        stc.append(ycor())
        stc.append(heading())

    elif ch == "]":
        penup()
        setheading(stc.pop())
        sety(stc.pop())
        setx(stc.pop())
        dl = stc.pop()
        thick = stc.pop()
        pensize(thick)
        pendown()

update()
mainloop()