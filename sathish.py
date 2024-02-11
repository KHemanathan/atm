import turtle

#turtle.Screen

turtle.bgcolor("black")
turtle.up()
turtle.setpos (-200, 250)
turtle.color("White")
turtle.down()
turtle.write("CAD POINT", font=("Lucida Calligraphy", 35))


turtle.up()
turtle.color("red")
turtle.fillcolor("red")

# Diya
turtle.setpos (-150, 100)
turtle.down()
turtle.right(90)
turtle.begin_fill()
turtle.circle(150, 180)
turtle.left(90)
turtle.forward (300)
turtle.end_fill()


turtle.up()
turtle.color("black")
turtle.back(150)
turtle.right (90)
turtle.down()
turtle.forward(30)
turtle.right(90)

# Lamp 
turtle.up()
turtle.color("#FFA500")
turtle.fillcolor("#FFA500")
turtle.begin_fill()
turtle.setpos (-50, 152)
turtle.right(90)
turtle.down()

turtle.circle(50, 180)
turtle.left(30)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()

turtle.up()
turtle.setpos (-340, -200)
turtle.color("White")
turtle.down()
turtle.write("HAPPY DIWALI", font=("Lucida Calligraphy", 55))

# Function Fire_Crackers
def move_to(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
# Fire_Cracker 1
move_to(-350,150)
turtle.color("red")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-350,150)
    angle+=18
    turtle.left(angle)
    turtle.write("\n IT TRAINING\n SERVICES & ", font=("Lucida Calligraphy", 20))
#1 Fire_Cracker 2
move_to(300,150)
turtle.color("red")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(300,150)
    angle+=18
    turtle.left(angle)
    turtle.write("DESIGNING CENTER", font=("Lucida Calligraphy", 20))
#Fire_Cracker 3
move_to(400,10)
turtle.color("yellow")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(400,10)
    angle+=18
    turtle.left(angle)
    turtle.write("AUTOCAD", font=("Lucida Calligraphy", 20))
# Fire_Cracker 4
move_to(450,-150)
turtle.color("blue")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(450,-150)
    angle+=18
    turtle.left(angle)
    turtle.write("CATIA\nSOLIDWORKS", font=("Lucida Calligraphy", 20))
# Fire_Cracker 5
move_to(370,-300)
turtle.color("violet")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(370,-300)
    angle+=18
    turtle.left(angle)
    turtle.write("REVIT\nSKETCHUP", font=("Lucida Calligraphy", 20))
# Fire_Cracker 6
move_to(-500,50)
turtle.color("yellow")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-500,50)
    angle+=18
    turtle.left(angle)
    turtle.write("C,C++,C#", font=("Lucida Calligraphy", 20))
# Fire_Cracker 7
move_to(-550,-100)
turtle.color("blue")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-550,-100)
    angle+=18
    turtle.left(angle)
    turtle.write("JAVA,PYTHON\nDATA SCIENCE,DEVOPS", font=("Lucida Calligraphy", 20))
# Fire_Cracker 8
move_to(-500,-300)
turtle.color("violet")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-500,-300)
    angle+=18
    turtle.left(angle)
    turtle.write("HTML,CSS\nSQL,PLSQL", font=("Lucida Calligraphy", 20))
# Fire_Cracker 9
move_to(-200,-300)
turtle.color("orange")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-200,-300)
    angle+=18
    turtle.left(angle)
    turtle.write("Mob:8099238708/8341292124\n Old Busstand,Chittoor", font=("Lucida Calligraphy", 20))
# Fire_Cracker 10
move_to(375,300)
turtle.color("green")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(375,300)
    angle+=18
    turtle.left(angle)
# Fire_Cracker 11
move_to(-500,300)
turtle.color("green")
angle=0
for i in range(20):
    turtle.fd(50)
    move_to(-500,300)
    angle+=18
    turtle.left(angle)

turtle.up()
turtle.setpos (400, -240)
turtle.color("Yellow")
turtle.down()
turtle.write(" ", font=("Arial", 20))
turtle.hideturtle()
turtle.exitonclick()
