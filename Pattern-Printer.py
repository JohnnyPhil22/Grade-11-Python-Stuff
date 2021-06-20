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
'''
   A
  BAB
 CBABC
DCBABCD
'''
for i in range(0,4):
    for sp in range(6,i,-1):
        print(' ',end='')
    for d in range(65+i,64,-1):
        print(chr(d),end='')
    for a in range(66,66+i,1):
        print(chr(a),end='')
    print('')
'''
   A
  ABA
 ABCBA
ABCDCBA
'''
