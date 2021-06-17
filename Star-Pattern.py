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

'''
