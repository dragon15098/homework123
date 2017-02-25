from turtle import *
def hinhvuong(solan, dodai, dodam):
    pensize(dodam)
    for i in range(solan):
        for j in range(4):
            forward(dodai)
            left(90)
        left(360/solan)
bgcolor("green")
color("pink")
speed(-1)
hinhvuong(50, 100 ,1)
        
