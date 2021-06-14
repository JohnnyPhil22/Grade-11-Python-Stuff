'''
1
12
123
1234
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

'''
1
22
333
4444
55555
'''
# Nested for loop
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()
# Single for loop
for i in range(1,6):
    print(str(i)*i,end='')
    print()
