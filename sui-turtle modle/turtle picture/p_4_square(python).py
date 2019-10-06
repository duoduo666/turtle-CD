import turtle

def moveon50():
    turtle.forward(50)

def moveright50():
    turtle.right(90)
    turtle.forward(50)   
    
def moveright100():
    turtle.right(90)
    turtle.forward(100)  
    
def turnright():
    turtle.right(90)


def p_4_square():
    colours=["red","blue","purple","brown"]
    x = 0
    while x < len(colours):
        turtle.pencolor(colours[x])
        moveon50()
        turnright()
        moveon50()
        moveright100()
        moveright100()
        x += 1

p_4_square()