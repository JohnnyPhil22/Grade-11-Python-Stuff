# While loop
n=int(input("Enter number: "))
s,i=0,1
while i<n:
    if(n%i==0):
        s+=i
    i+=1
if s==n:
    print("It's a perfect number.")
else:
    print("It isn't a perfect number.")       
# For loop
n=int(input("Enter number: "))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if s==n:
    print("It's a perfect number.")
else:
    print("It isn't a perfect number.")
