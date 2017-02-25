from turtle import *
def hinhvuong(solan, dodai):
    right(90)    
    for i in range (solan*4):
        forward(dodai)
        left(90)
        dodai = dodai +2       
speed(-1)
bgcolor("green")
color("blue")
hinhvuong(20,10)
