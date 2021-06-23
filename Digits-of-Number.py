# All digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    print(d)
    n//=10
# Even digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    n//=10
    if d%2==0:
        print(d)
# Odd digits
n=int(input("Enter number: "))
while n>0:
    d=n%10
    n//=10
    if d%2!=0:
        print(d)
# Sum of digits
n=int(input("Enter number: "))
s=0
while n>0:
    d=n%10
    n//=10
    s+=d
print("Sum of digits:",s)
# Reverse of number
n=int(input("Enter number: "))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n//=10
print("Reversed number:",r)
# Largest digit

# Number of odd digits
