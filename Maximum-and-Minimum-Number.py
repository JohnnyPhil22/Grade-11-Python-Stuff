n=int(input("Enter number < 0: "))
maxno=n
minno=n
for i in range(1,10):
    n=int(input("Enter number < 0: "))
    if n>maxno:
        maxno=n
    if n<minno:
        minno=n
print("Maximum number:",maxno,"and Minimum number:",minno)
