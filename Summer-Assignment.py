# Print multiplication table of 10
for i in range(1, 11):
    p=10*i
    print("10 times",i,"=",p)
# Check validity of a date
d=int(input("Enter day (1 to 31): "))
m=int(input("Enter month (1 to 12): "))
y=int(input("Enter year: "))
if y%4==0 and m==2 and d==29:
    print("It is a valid date.")
elif y%4==0 and 0<m<=12 and 1<=d<=31:
    print("It is a valid date.")
elif (m==1 or m==3 or m==5 or m==7 or m==9 or m==11) and d<=31:
    print("It is a valid date.")
elif (m==4 or m==6 or m==8 or m==10 or m==12) and d<=30:
    print("It is a valid date.")
else:
    print("It is not a valid date.")
# First ‘n’ Fibonacci numbers
n=int(input("Enter number: "))
f1,f2=0,1
print(f1, end=" ")
for x in range(1,n):
    print(f2,end=" ")
    next=f1+f2
    f1=f2
    f2=next
'''Menu driven program to find the sum of the following series:
1. 1+x2+x3+x4+...
2. x-x2/3!+x3/5!-x4/7!+...
'''
opt='y'
while opt in 'Yy':
    print('1. 1+x2+x3+x4+...')
    print('2. x-x2/3!+x3/5!-x4/7!+...')
    ch=int(input("Enter your choice: "))
    if ch==1:
        x=int(input("Enter the value of x: "))
        n=int(input("Enter the value of n: "))
        s=1
        for i in range(2,n+1,1):
            s+=x**i
        print('Sum of series: ',s)
    elif ch==2:
        x=int(input("Enter the value of x: "))
        n=int(input("Enter the value of n: "))
        s,p,f=0,1,1
        for i in range(1,n+1):
            for j in range(1,2*i):
                p*=j
                if f==1:
                    s+=(i*x)/p
                    f,p=0,1
                elif f==0:
                    s-=(i*x)/p
                    f,p=1,1
        print('Sum of series: ',s)
    else:
        print("Select from options 1 through 2.")
    opt=input('Press y to continue: ')
'''Write a menu driven program to perform the following tasks:
1) Find the factorial of a number
2) Find the sum of the digits of a number
3) Check whether a number is palindrome or not
4) Check whether a number is Armstrong or not
5) Check whether a number is prime or not
6) Exit
'''
opt="y"
while opt in "yY":
    print("1. Find factorial of number.")
    print("2. Find sum of digits of number.")
    print("3. Check whether number is palindrome or not.")
    print("4. Check whether number is Armstrong number or not.")
    print("5. Check whether number is prime or not.")
    print("6. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        n = int(input("Enter a number: "))
        fact=1
        for i in range(1,n+1):
            fact*=i
        print("Factorial of number:",fact)
    elif ch==2:
        n=int(input("Enter number: "))
        s=0
        while n>0:
            d=n%10
            n//=10
            s+=d
        print("Sum of digits:",s)
    elif ch==3:
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
    elif ch==4:
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
    elif ch==5:
        n=int(input("Enter number: "))
        for i in range(2,n//2+1):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")
    elif ch==6:
        print("")
    else:
        print("Select between options 1 and 2.")
    opt=input("Press y to continue: ")
'''
Write a menu – driven program to print the following series:
i. 1
   22
   333
   4444
ii. A
    AAA
    AAAAA
'''
opt="y"
while opt in "yY":
    print("1. 1\n 22\n 333\n 4444")
    print("2. A\n AAA\n AAAAA")
    ch=int(input("Enter choice: "))
    if ch==1:
        for i in range(1,5):
            print(str(i)*i,end='')
            print('')
    elif ch==2:
        for i in range(1,6,2):
            for j in range(1,i+1):
                if j%2==0:
                    print("A",end='')
                else:
                    print("A",end='')
        print('')
     else:
        print("Select between options 1 and 2.")
     opt=input("Press y to continue: ")
# Calculate sum and average of odd, even and prime number.
min=int(input("Enter Minimum Value: "))
max=int(input("Enter Maximum Value: "))
etot,otot,ptot=0,0,0
ecount,ocount,pcount=0,0,0
for i in range(min,max+1):
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
            if f==0 and i!=1:
                ptot+=i
                pcount+=1
for n in range(min,max+1):
    if n%2==0:
        etot+=n
        ecount+=1
    else:
        otot+=n
        ocount+=1
eavg=etot/ecount
oavg=otot/ocount
pavg=ptot/pcount
print("Sum of Even Numbers:",etot)
print("Average of Even Numbers:",eavg)
print("Sum of Odd Numbers:",otot)
print("Average of Odd Numbers:",oavg)
print("Sum of Prime Numbers:",ptot)
print("Average of Prime Numbers:",pavg)
# Find the sum of prime numbers between 2 ranges
ll=int(input("Enter lower limit: "))
ul=int(input("Enter upper limit: "))
tot=0
for i in range(ll,ul+1):
    if i==1:
        continue
    for j in range(2,i//2+1):
        if i%j==0:
            break
        else:
            tot+=i
print("Sum of all prime numbers:",tot)
# Calculate roots of a quadratic equation.
a = int(input("Enter coefficient for first term in quadratic equation: "))
b = int(input("Enter coefficient for second term in quadratic equation: "))
c = int(input("Enter coefficient for third term in quadratic equation: "))
if a==0:
    print("a cannot be zero.")
else:
    d = (b**2)-(4*a*c)
    if d>0:
        root1 = (-b-(d**0.5))/(2*a)
        root2 = (-b+(d**0.5))/(2*a)
        print("The solutions are",root1,"and",root2,".")
    elif d==0:
        root = -b/(2*a)
        print("The solutions are",root,"and",root,".")
    else:
        print("The solutions are complex and imaginary.")
