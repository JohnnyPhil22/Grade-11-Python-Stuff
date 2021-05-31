radius=float(input("Enter length of radius: "))
choice=input("Enter if you want Area/Both/Circumference (A/B/C): ")
if choice=="A":
    area=3.14*(radius**2)
    print("Area of Circle:",area)
if choice=="B":
    circ=3.14*2*radius
    area=3.14*(radius**2)
    print("Area of Circle:",area,". Circumference of Circle:",circ)
if choice=="C":
    circ=3.14*2*radius
    print("Circumference of Circle:",circ)
