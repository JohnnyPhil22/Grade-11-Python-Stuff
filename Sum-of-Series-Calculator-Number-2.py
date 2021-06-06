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
