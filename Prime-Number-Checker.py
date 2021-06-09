# Simple for loop
n=int(input("Enter number: "))
f=0
for i in range(2,n//2+1):
    if n%i==0:
        f=1
if f==0:
    print("Prime")
else:
    print("Not Prime")
    
# For... else loop
n=int(input("Enter number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
