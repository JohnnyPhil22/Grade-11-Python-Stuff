ll=int(input("Enter lower limit: "))
ul=int(input("Enter upper limit: "))
for i in range(ll,ul+1):
    if i==1:
        continue
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)
