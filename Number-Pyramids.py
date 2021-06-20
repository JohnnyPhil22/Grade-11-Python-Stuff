'''
   1
  212
 32123
4321234
'''
for i in range(1,5):
    for sp in range(6,i,-1):
        print(' ',end='')
    for d in range(i,0,-1):
        print(d,end='')
    for a in range(2,i+1):
        print(a,end='')
    print('')
