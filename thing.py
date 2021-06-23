opt='y'
while opt in 'yY':
    print("1. Area of circle")
    print("2. Circumference of circle")
    print("3. Area of rectangle")
    print("4. Perimeter of rectangle")
    ch=int(input("Enter choice: "))
    if ch==1:
        r=int(input("Enter radius: "))
        print("Area of circle:",(3.14*(r**2)))
    elif ch==2:
        r=int(input("Enter radius: "))
        print("Circumference of circle:",(2*3.14*r))
    elif ch==3:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("Area of rectangle:",(l*b))
    elif ch==4:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("Perimeter of rectangle:",(2*(l+b)))
    else:
        print("Select from options 1 through 4.")
    opt=("Press y to continue: ")
