from turtle import *
def draw_poly(n, sz):
    for i in range(n):
        forward(sz)
        left(360/n)
speed(-1)
pensize(3)
color("pink")
bgcolor("green")
draw_poly(8, 50)
        
