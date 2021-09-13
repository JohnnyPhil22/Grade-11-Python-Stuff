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
for i in range(0,4):
    for sp in range(i,6):
        print(' ',end='')
    for d in range(65,65+i):
        print(chr(d),end='')
    for a in range(65+i,64,-1):
        print(chr(a),end='')
    print('')
'''
    A
   B C
  D E F
 G H I J
K L M N O
'''
n=65
for i in range(0,5):
    for sp in range(i,6):
        print(' ',end='')
    for j in range(0,i+1):
        print(chr(n),end=' ')
        n+=1
    print('')

'''
Given string 'abc', print following patterns:
a. a
   bb
   ccc
b. a
   ab
   abc
c. abc
   ab
   a
d. cba
   cb
   c
e. a
   abab
   abcabcabc
'''
str='abc'
# 1st Sub Part
for i in range(0,3):
    for j in range(0,i+1):
        print(str[i],end='')
    print()
# 2nd Sub Part
for i in range(1,4):
    for j in range(0,i):
        print(str[j],end='')
    print()
# 3rd Sub Part
for i in range(3,0,-1):
    for j in range(0,i):
        print(str[j],end='')
    print()
# 4th Sub Part
for i in range(-1,2,1):
    for j in range(2,i,-1):
        print(str[j],end='')
    print()
# 5th Sub Part
for i in range(1,4):
    for r in range(1,i+1):
        for j in range(0,i):
            print(str[j],end='')
    print()
