a = int(input("Enter coefficient for first term in quadratic equation: "))
b = int(input("Enter coefficient for second term in quadratic equation: "))
c = int(input("Enter coefficient for third term in quadratic equation: "))

if a==0:
    print("a cannot be zero.")
else:
    d = (b**2)-(4*a*c)

    if d>0:
        root1 = (-b-(d**0.5))/(2*a)
        root2 = (-b+(d**0.5))/(2*a)
        print("The solutions are",root1,"and",root2,".")
    elif d==0:
        root = -b/(2*a)
        print("The solutions are",root,"and",root,".")
    else:
        print("The solutions are complex and imaginary.")
