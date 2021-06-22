ll=int(input("Enter lower limit: "))
ul=int(input("Enter upper limit: "))
# Nested for loop
print("Nested for loop")
for i in range(ll,ul+1):
    if i==1:
        continue
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i,end=' ')
print('')
# Break
print("Break")
for i in range(ll,ul+1):
    if i==1:
        continue
    n=i
    for j in range(2,i//2+1):
        if n%j==0:
            break
    else:
        print(n,end=' ')
print('')
# Flag
print("Flag")
for i in range(ll,ul+1):
    n,f=i,0
    if i==1:
        continue
    for j in range(2,i//2+1):
        if n%j==0:
            f=1
    if f==0:
        print(n,end=' ')
print('')
# While
print("While")
while ll<=ul:
    n,f=ll,0
    if i==1:
        continue
    for j in range(2,n//2+1):
        if n%j==0:
            f=1
    if f==0:
        print(n,end=' ')
    ll+=1
