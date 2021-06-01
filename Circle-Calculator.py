print("1. Perimeter")
print("2. Area")
ch=input("Enter your choice: ")
ra=float(input("Enter length of radius: "))
if ch=="2":
    ar=3.14*(ra**2)
    print("Area of Circle:",ar,"square units.")
elif ch=="1":
    ci=2*3.14*ra
    print("Circumference of Circle:",ci,"units.")
else:
    print("Please select from only 1 or 2...")
