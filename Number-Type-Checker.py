# Palindrome checker

# Armstrong checker
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
