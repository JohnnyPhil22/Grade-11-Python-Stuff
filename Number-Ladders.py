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
'''
1
10
101
1010
10101
'''
for i in range(1,6):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print('')
'''
1
101
10101
1010101
'''
for i in range(1,8,2):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print('')
'''
55555
4444
333
22
1
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end='')
    print()
