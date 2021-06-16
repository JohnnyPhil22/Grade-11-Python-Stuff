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
55555
4444
333
22
1
'''

'''
*****
****
***
**
*
'''

'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
