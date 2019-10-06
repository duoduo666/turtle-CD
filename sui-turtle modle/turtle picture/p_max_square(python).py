import turtle



def p_max_square():
    turtle.speed(999)
    for i in range(360):
        turtle.setheading(i)
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)

turtle.speed(999)
p_max_square()