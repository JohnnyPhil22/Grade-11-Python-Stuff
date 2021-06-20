'''
*
**
***
****
*****
'''
for i in range(1,6):
    print("*"*i)
'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print('')
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
   *
  *** 
 *****
*******
'''
for i in range(1,8,2):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
* * * * *
 * * * *
  * * *
   * *
    *
'''
for i in range(5,0,-1):
    for sp in range(i,6,1):
        print(' ',end='')
    for j in range(i,0,-1):
        print('* ',end='')
    print('')
'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
for i in range(1,6):
    for sp in range(6,i,-1):
        print(' ',end='')
    for j in range(0,i):
        print('* ',end='')
    print('')
for i in range(4,0,-1):
    for sp in range(i,6,1):
        print(' ',end='')
    for j in range(i,0,-1):
        print('* ',end='')
    print('')
'''
     *
    * *
   *   *
  *     *
 *       *
***********
'''
k=0
for i in range(1,7):
    for j in range(i,6):
        print(' ',end='')
    while k!=(2*i-1):
        if k==0 or k==2*i-2:
            print('*', end='')
        else:
            print(' ', end='')
        k+=1
    k=0
    print('')
for i in range(0, 11):
    print('*', end='')
print('')
