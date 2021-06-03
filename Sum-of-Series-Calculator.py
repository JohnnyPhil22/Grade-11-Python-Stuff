x = int(input("Enter a number: "))
n = int(input("Enter a power: "))
s = 0
for i in range(1,n+1):
    s = s+(x**i)
print("Sum of series:",s)
