'''
$
@@
$$$
@@@@
$$$$$
'''
# Simple For Loop
for i in range(1,6):
    if i%2==0:
        print("@"*i,end='')
    else:
        print("$"*i,end='')
    print('')
# Nested For Loop
for i in range(1,6):
    for j in range(1,i+1):
        if i%2==0:
            print("@",end='')
        else:
            print("$",end='')
    print('')
'''
A
AB
ABC
ABCD
ABCDE
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print('')
