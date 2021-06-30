import turtle
wn=turtle.Screen()
wn.setup(1600,1200)
wn.title("Farewell message to Viji ma'am from 11 Science H")
wn.bgcolor('black')
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,150)
pen.write("Farewell message to Viji ma'am from 11 Science H",align="center",font=("Ubuntu",24,"bold"))
pen.goto(0,-150)
pen.write("Good morning ma'am!\nMa'am, since today is\nthe last day you will be\nwith us, we now present\nour small 'surprise' from\nall of us 11 Sci H students...",align="center",font=("Ubuntu",24,"bold"))

while True:
    wn.mainloop()