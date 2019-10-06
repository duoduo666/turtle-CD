import turtle

#移动

#移动（50）
def moveon50():
    turtle.forward(50)
def moveback50():
    turtle.right(180)
    turtle.forward(50)
def moveleft50():
    turtle.right(270)
    turtle.forward(50)
def moveleft50():
    turtle.right(270)
    turtle.forward(50)
#移动（100）
def moveon100():
    turtle.forward(100)
def moveback100():
    turtle.right(180)
    turtle.forward(100)
def moveleft100():
    turtle.right(270)
    turtle.forward(100)    
def moveleft100():
    turtle.right(270)
    turtle.forward(100)


#转向（矩形）
def turnleft():
    turtle.left(90)
def turnright():
    turtle.right(90)
#一个整的方形
def whole_spuare_50():
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
#三个合并的方形
def big_square_50_100_200():
    big_square_x = 0
    while big_square_x <= 2:
        turtle.forward(50)
        turtle.right(90)
        big_square_x += 1
    while big_square_x > 2 and big_square_x <= 6:
        turtle.forward(100)
        turtle.right(90)
        big_square_x += 1
    while big_square_x > 6 and big_square_x <= 9:
        turtle.forward(200)
        turtle.right(90)
        big_square_x += 1
    turtle.forward(200)
    
#转向（正三角形）
def tir_left():
    turtle.left(60)
def tri_right():
    turtle.right(60)
#整个三角形
def whole_tir_50():
    turtle.right(120)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)
#三个三角形合并
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

#转向（正五边形）
def pen_left():
    turtle.left(72)

def pen_right():
    turtle.right(72)
#整个五边形
def whole_pen_50():
    penx = 0
    while penx < 5:
        turtle.forward(50)
        pen_left()
        penx += 1
#三个五边形合并
def big_pen_50_100_200():
    big_pen_x = 0
    while big_pen_x <= 5:
        turtle.right(72)
        turtle.forward(50)
        big_pen_x += 1
    while big_pen_x > 5 and big_pen_x <= 10:
        turtle.right(72)
        turtle.forward(100)
        big_pen_x += 1
    while big_pen_x > 10 and big_pen_x <= 15:
        turtle.right(72)
        turtle.forward(200)
        big_pen_x += 1

#六边形转向
def hex_left():
    turtle.left(60)

def hex_right():
    turtle.right(60)

#整个六边形
def whole_hex_50():
    hexx = 0
    while hexx < 5:
        turtle.forward(50)
        hex_left()
        hexx += 1

#三个六边形合并
def big_hex_50_100_200():
    big_hex_x = 0
    while big_hex_x <= 6:
        turtle.right(60)
        turtle.forward(50)
        big_hex_x += 1
    while big_hex_x > 6 and big_hex_x <= 12:
        turtle.right(60)
        turtle.forward(100)
        big_hex_x += 1
    while big_hex_x > 12 and big_hex_x <= 18:
        turtle.right(60)
        turtle.forward(200)
        big_hex_x += 1

#前缀函数结束        
def p_max_square():
    turtle.speed(999)
    for i in range(90):
        turtle.right(1)
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)

#最终函数开始
def p_tri_squ_pen_hex():
    color=["red","blue","purple","brown","black","yellow","green"]
    for i in range(4):
        for i in range(5):
            turtle.pencolor(color[i])
            turtle.forward(50)
            hex_left()
        turtle.right(60)
    turtle.penup()
    hex_left()
    turtle.forward(50)
    turtle.left(60)
    moveon100()
    moveon100()
    moveon50()
    turtle.right(90)
    moveon50()
    turtle.right(60)
    turtle.pendown()
    for x in range(4):
        for j in range(3):
            turtle.pencolor(color[j])
            big_tri_50_100_200()
            turtle.right(60)
        turtle.left(60)
        moveback100()
        moveon100()
        turnright()
        for k in range(3):
            turtle.pencolor(color[k])
            whole_hex_50()
            turtle.right(60)
            moveon50()
        moveon100()
        whole_hex_50()
        moveon50()
        turtle.pencolor("green")
        turtle.right(30)
        p_max_square()
        moveback100()
        moveon100()
        turtle.right(60)
    
    
turtle.speed(999)        
p_tri_squ_pen_hex()