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
