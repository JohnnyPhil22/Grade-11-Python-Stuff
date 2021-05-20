import math

base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
ArM1 = (base*height)/2
print("Area of triangle is",ArM1,".")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
side1 = int(input("Enter length of first side: "))
side2 = int(input("Enter length of second side: "))
side3 = int(input("Enter length of third side: "))
s = (side1+side2+side3)/2
ArM2 = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print("Area of triangle is",ArM2,".")
