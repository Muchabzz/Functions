import turtle

def draw_square(length):
    pen = turtle.Turtle() #Tworzy żółwia
    pen.speed(3)

    for i in range(4):
        pen.forward(length) #Żółw idzie do przodu o length
        pen.right(90)  #Żółw obraca się w prawo o 90 stopni.

    pen.hideturtle()