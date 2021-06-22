ll = int(input("Enter lower limit: "))
ul = int(input("Enter upper limit: "))
for i in range(ll, ul+1):
    if i==1:
        continue
    f=1
    for j in range(2,i//2+1):
        if i%j==0:
            f=0
            break
    if f==1:
        print(i)
