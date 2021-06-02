n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
sum1 = n1+n2+n3
print("Sum of all numbers is:",sum1,".")
if n1==n2:
    sum2 = n1+n3
    print("Sum of all non-repeating numbers is:",sum2,".")
elif n1==n3:
    sum2 = n1+n2
    print("Sum of all non-repeating numbers is:",sum2,".")
elif n2==n3:
    sum2 = n2+n1
    print("Sum of all non-repeating numbers is:",sum2,".")
