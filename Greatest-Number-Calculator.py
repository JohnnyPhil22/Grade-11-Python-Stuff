# Simple if
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
if n1>n2>n3:
    print(n1,"is greater.")
if n2>n1>n3:
    print(n2,"is greater.")
if n3>n1>n2:
    print(n3,"is greater.")

# Nested if
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
if n1>n2>n3:
    print(n1,"is greater.")
elif n2>n1>n3:
    print(n2,"is greater.")
else:
    print(n3,"is greater.")
