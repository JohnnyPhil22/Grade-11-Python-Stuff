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
'''
1
3 2
6 5 4
10 9 8 7
'''
start,stop=1,2
current_num=stop
for r in range(2,6):
    for c in range(start,stop):
        current_num-=1
        print(current_num,end=' ')
    print("")
    start=stop
    stop+=r
    current_num=stop
'''
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
for i in range(0,5):
    n=i+1
    inc=4
    for j in range(0,i+1):
        print(n,end=' ')
        n+=inc
        inc-=1
    print('')
