# Palindrome checker
n=int(input("Enter number: "))
r,dn=0,n
while n>0:
    d=n%10
    r=r*10+d
    n//=10
print(r)
if r==dn:
    print("Number is a palindrome.")
else:
    print("Number is not a palindrome.")
# Armstrong number checker
n=int(input("Enter number: "))
s,dn=0,n
while dn>0:
    d=dn%10
    s+=d**3
    dn//=10
print(s)
if s==n:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
