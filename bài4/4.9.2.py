from turtle import *
def hinhvuong(solan, dodai, dodam):
    pensize(dodam)
    for i in range(solan):
        for j in range(4):
            forward(dodai)
            left(90)
        penup()
        goto(-10*(i+1),-10*(i+1))
        dodai = dodai + 20
        pendown()
bgcolor("green")
color("pink")
hinhvuong(4,20,3)
        
