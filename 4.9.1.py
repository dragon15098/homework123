from turtle import *
def hinhvuong(solan, dodai, dodam):
    pensize(dodam)
    for i in range(solan):
        for j in range (4):
            forward(dodai)
            left(90)
        penup()
        forward(dodai*2)
        pendown()
speed(-1)
bgcolor("green")
color("pink", "pink")
hinhvuong(5, 20, 3)
