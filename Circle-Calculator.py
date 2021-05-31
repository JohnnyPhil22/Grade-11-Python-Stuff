ra=float(input("Enter length of radius: "))
ch=input("Enter if you want Area/Circumference/Both for your circle (A/B/C): ")
ar=3.14*(ra**2)
ci=2*3.14*ra
if ch=="A":
    print("Area of Circle:",ar,"square units.")
elif ch=="C":
    print("Circumference of Circle:",ci,"units.")
elif ch=="B":
    print("Area of Circle:",ar,"square units. Circumference of Circle:",ci,"units.")
