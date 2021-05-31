radius=float(input("Enter length of radius: "))
choice=input("Enter if you want Area/Circumference/Both for your circle (A/B/C): ")
area=3.14*(radius**2)
circ=3.14*2*radius
if choice=="A":
    print("Area of Circle:",area,"square units.")
elif choice=="C":
    print("Circumference of Circle:",circ,"units.")
elif choice=="B":
    print("Area of Circle:",area,"square units. Circumference of Circle:",circ,"units.")
