n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Operators:\n1. + for addition\n2. - for subtraction\n3. * for multiplication\n4. / for division\n5. // for integer division\n6. % for modulus\n7. ** for exponentiation")
op = input("Enter an arithmetic operator (1 to 7): ")
if op=="1":
    re=n1+n2
    print("Sum is:",re,".")
elif op=="2":
    re=n1-n2
    print("Difference is:",re,".")
elif op=="3":
    re=n1*n2
    print("Product is:",re,".")
elif op=="4":
    re=n1/n2
    print("Complete quotient is:",re,".")
elif op=="5":
    re=n1//n2
    print("Quotient is:",re,".")
elif op=="6":
    re=n1%n2
    print("Remainder of division is:",re,".")
elif op=="7":
    re=n1**n2
    print("Power is:",re,".")
else:
    print("Please enter a number from 1 to 7...")
