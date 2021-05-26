# With if... else
no1=int(input("Enter first number: "))
no2=int(input("Enter second number: "))
if no2%no1==0:
    print("The second number is divisible by the first number.")
else:
    print("The second number is not divisible by the first number.")

# Without if... else
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
rem = x%y
print("The numbers are divisible: ",rem==0)
