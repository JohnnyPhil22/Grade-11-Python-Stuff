r = int(input("Enter radius of circle (in centimeters): "))
ar = 3.141592653589793 * (r**2)
c = 2 * 3.141592653589793 * r
req = input("Do you want area of circle or circumference or both (A - Area, B - Both, C - Circumference): ")
if req == "A":
    print("The area of the circle is ", ar, " square centimeters.")
if req == "B":
    print("The area of the circle is ", ar, " square centimeters. The circumference of the circle is ", c, " centimeters.")
if req == "C":
    print("The circumference of the circle is ", c, " centimeters.")
