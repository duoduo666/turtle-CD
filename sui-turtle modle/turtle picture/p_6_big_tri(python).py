import turtle

def big_tri_50_100_200():
    big_tri_x = 0
    while big_tri_x <= 2:
        turtle.right(120)
        turtle.forward(50)
        big_tri_x += 1
    while big_tri_x > 2 and big_tri_x <= 5:
        turtle.right(120)
        turtle.forward(100)
        big_tri_x += 1
    while big_tri_x > 5 and big_tri_x <= 8:
        turtle.right(120)
        turtle.forward(200)
        big_tri_x += 1
x = 0
colours = ["red","blue","green","brown","black","purple"] 
while x < 6:
    turtle.pencolor(colours[x])
    turtle.left(60)
    big_tri_50_100_200()
    x += 1