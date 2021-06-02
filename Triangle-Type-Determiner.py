a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))
if a==b==c:
    print("The triangle is equilateral.")
else:
    if a==b or b==c or c==a:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
