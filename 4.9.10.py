from turtle import * 
def ve_ngoi_sao(sz):
    for j in range (5):
        for i in range (5):
            forward(sz)
            right(144)
        penup()
        forward(350)
        right(144)
        pendown()
speed(-1)
penup()
goto(-100,100)
pendown()
bgcolor("green")
color("pink")
ve_ngoi_sao(100)

    
