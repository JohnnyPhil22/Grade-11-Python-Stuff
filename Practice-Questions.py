'''
    *
  * * *
* * * * *
  * * *
    *
'''
for i in range(1,6,2):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
for i in range(3,0,-2):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
1010101
 10101
  101
   1
'''
for i in range(7,0,-2):
    for sp in range(i,6,1):
        print(' ', end='')
    for j in range(1,i+1):
        if j%2==0:
            print("0",end='')
        else:
            print("1",end='')
    print('')
'''
*
**
***
****
*****
****
***
**
*
'''
for i in range(1,6):
    print("*"*i)
for i in range(4):
    for j in range(4-i):
        print("*",end="")
    print('')
