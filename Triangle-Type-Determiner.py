a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))
if a<=0 or b<=0 or c<=0:
    print("Please enter a value greater than 0.")
elif a==b==c:
    print("The triangle is equilateral.")
else:
    if a==b or b==c or c==a:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
