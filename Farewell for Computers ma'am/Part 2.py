import turtle
from PIL import Image
wn=turtle.Screen()
wn.setup(1600,1200)
wn.title("Farewell message to Viji ma'am from 11 Science H")
wn.bgcolor('black')
wn.tracer(0)

image = Image.open('/home/jonathanvijayphilips/Desktop/Thing/Picture.png')
image.show()

while True:
    wn.mainloop()