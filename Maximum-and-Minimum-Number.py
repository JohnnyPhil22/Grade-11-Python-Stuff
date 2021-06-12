import math
maxno=-math.inf
minno=math.inf
for i in range(1,11):
    n=int(input("Enter number < 0: "))
    if n>maxno:
        maxno=n
    if n<minno:
        minno=n
print("Maximum number:",maxno,"and Minimum number:",minno)
