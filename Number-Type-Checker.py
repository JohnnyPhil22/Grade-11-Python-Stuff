# Palindrome checker

# Armstrong checker
n=int(input("Enter number: "))
s,temp=0,n
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10
print(s)
if s==n:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
