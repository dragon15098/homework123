from turtle import *
speed(-1)
def draw_poly(n, sz):
    for i in range(n):
        forward(sz)
        left(360/n)
def draw_equitriangle(t, sz):
    draw_poly(t,sz)
speed(-1)
bgcolor("green")
color("pink")
draw_equitriangle(3,100)
