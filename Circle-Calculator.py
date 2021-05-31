ra=float(input("Enter length of radius: "))
ch=input("Enter if you want Area/Circumference/Both for your circle (A/B/C): ")
ar=3.14*(ra**2)
ci=3.14*2*ra
if choice=="A":
    print("Area of Circle:",ar,"square units.")
elif choice=="C":
    print("Circumference of Circle:",ci,"units.")
elif choice=="B":
    print("Area of Circle:",ar,"square units. Circumference of Circle:",ci,"units.")
