a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))

if c>(a+b) or a>(b+c) or b>(c+a):
    print("These are sides of a triangle.")
else:
    print("These are not sides of a triangle.")
