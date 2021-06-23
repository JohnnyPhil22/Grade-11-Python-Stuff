n=int(input("Enter number: "))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n//=10
print("Reversed number:",r)
