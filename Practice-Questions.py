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
'''
* * * * * * *
* * * * *
* * *
*
* * *
* * * * *
* * * * * * *
'''
for i in range(7,1,-2):
    for j in range(0,i):
        print('* ',end='')
    print('')
for i in range(1,8,2):
    for j in range(0,i):
        print('* ',end='')
    print('')
'''
1 2 3 4 5 6
2 3 4 5 6
3 4 5 6
4 5 6
5 6
6
'''
for i in range(0,6):
    for j in range(1,7-i,1):
        print(j,end=' ')
    print('')
'''
        0
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
'''
for i in range(0,5):
    for sp in range(6,i,-1):
        print(' ',end=' ')
    for d in range(i,-1,-1):
        print(d,end=' ')
    for a in range(1,i+1):
        print(a,end=' ')
    print('')
'''
ABCDEFGFEDCBA
ABCDEFFEDCBA
ABCDEEDCBA
ABCDDCBA
ABCCBA
ABBA
AA
'''
for i in range(71,64,-1):
    for j in range(65,i+1):
        print(chr(j),end='')
    for k in range(i,64,-1):
        print(chr(k),end='')
    print('')
'''
#*#*#*#*#
*#*#*#*#
#*#*#*
*#*#*
#*#
*#
#
'''
for i in range(6,-3,-1):
    for j in range(1,i+4):
        if i%2==0:
            if j%2==0:
                print("*",end='')
            else:
                print("#",end='')
        else:
            if j%2!=0:
                print("*",end='')
            else:
                print("#",end='')
    print('')
'''
 ***
*   *
*   *
*****
*   *
*   *
*   *
'''
for r in range(0,7):
    for c in range(0,7):
        if (((c==1 or c==5) and r!=0) or ((r==0 or r==3) and (c>1 and c<5))):
            print('*',end='')
        else:      
            print(' ',end='')
    print('')
# Highest Common Factor of two given numbers:
n1=int(input("Enter smaller number: "))
n2=int(input("Enter larger number: "))
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("Highest Common Factor:",hcf)
# FizzBuzz
for i in range(1,51):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# Vowel or consonant detector
l=str(input("Enter letter: "))
if 'A'<=l<='Z' or 'a'<=l<='z':
    if ord(l)==65 or ord(l)==69 or ord(l)==73 or ord(l)==79 or ord(l)==85 or ord(l)==97 or ord(l)==101 or ord(l)==105 or ord(l)==111 or ord(l)==117:
        print("Letter is a vowel.")
    else:
        print("Letter is a consonant.")
else:
    print("Enter only a letter.")
# Triangle determiner
a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))
if a<=0 or b<=0 or c<=0:
    print("Please enter a value greater than 0.")
elif a==b==c:
    print("The triangle is equilateral.")
else:
    if a==b or b==c or c==a:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
# Astrological sign
d = int(input("Input birthday: "))
m = input("Input month of birth: ")
if m=='December':
    if d<22:
        a='Sagittarius'
    else:
        a='Capricorn'
elif m == 'january':
    if d<20:
        a='Capricorn'
    else:
        a='Aquarius'
elif m=='February':
    if d<19:
        a='Aquarius'
    else:
        a='Pisces'
elif m=='March':
    if d<21:
        a='Pisces'
    else:
        a='Aries'
elif m=='April':
    if d<20:
        a='Aries'
    else:
        a='Taurus'
elif m=='May':
    if d<21:
        a='Taurus'
    else:
        a='Gemini'
elif m=='June':
    if d<21:
        a='Gemini'
    else:
        a='Cancer'
elif m == 'July':
    if d<23:
        a='Cancer'
    else:
        a='Leo'
elif m=='August':
    if d<23:
        a='Leo'
    else:
        a='Virgo'
elif m=='September':
    if d<23:
        a='Virgo'
    else:
        a='Libra'
elif m=='October':
    if d<23:
        a='Libra'
    else:
        a='Scorpio'
elif m=='November':
    if d<22:
        a='Scorpio'
    else:
        a='Sagittarius'
print("Astrological Sign:",a)
