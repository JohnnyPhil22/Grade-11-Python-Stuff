# s = x+x^2+x^3+x^4+...+x^n
x = int(input("Enter a number: "))
n = int(input("Enter a power: "))
s = 0
for i in range(1,n+1):
    s = s+(x**i)
print("Sum of series:",s)

# s = 1-1/3+1/5-1/7+1/9-1/11+...+1/n
n = int(input("Enter odd number: "))
f,s=0,0
for i in range(1,n+1,2):
    if f==0:
        s+=1/i
        f=1
    else:
        s-=1/i
        f=0
print(s)

# s = 1/2+3/2+...+n/2
n = int(input("Enter a number: "))
s = 0
for i in range(1,n+1,2):
    s+=i/2
print("Sum of series:",s)

# s = x+x/3+x/5+...+x/n
x = int(input("Enter a number: "))
n = int(input("Enter an odd number: "))
s = 0
for i in range(1,n+1,2):
    s+=x/i
print("Sum of series:",s)

# s = x/x^2+x/x^4+x/x^6+x/x^8+...+x/x^n
x = int(input("Enter a number: "))
n = int(input("Enter another number: "))
s = 0
for i in range(1,n+1,2):
    s+=x/(x**2)
print("Sum of series:",s)

# s = 1-1/x+1/x^2-1/x^3+1/x^4-1/x^5+...+1/x^n
x = int(input("Enter a number: "))
n = int(input("Enter an odd number: "))
s = 1
for i in range(1,n+1):
    if i%2==0:
        s+=1/(x**i)
    else:
        s-=1/(x**i)
print("Sum of series:",s)

# s = 1+2-2^2+2^3-2^4+...+2^n
n = int(input("Enter a number: "))
s = 1
for i in range(1,n+1):
    if i%2==0:
        s-=2**i
    else:
        s+=2**i
print("Sum of series:",s)
