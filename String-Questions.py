# Input a string and count number of times 'a', 'A' appear in the sentence.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='A':
        count+=1
print('Number of times \'a\' or \'A\' appear:',count)

# Input string and count number of vowels.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
       count+=1
print('Number of times vowels appear:',count)

# Input tring and count number of consonants.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    if s[i]!='a' or s[i]!='A' or s[i]!='e' or s[i]!='E' or s[i]!='i' or s[i]!='I' or s[i]!='o' or s[i]!='O' or s[i]!='u' or s[i]!='U':
        count+=1
print('Number of times consonants appear:',count)

# Input string and count number of characters.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    count+=1
print('Number of characters appear:',count)

# Input string and count number of lowercase characters.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='b' or s[i]=='c' or s[i]=='d' or s[i]=='e' or s[i]=='f' or s[i]=='g' or s[i]=='h' or s[i]=='i' or s[i]=='j' or s[i]=='k' or s[i]=='l' or s[i]=='m' or s[i]=='n' or s[i]=='o' or s[i]=='p' or s[i]=='q' or s[i]=='r' or s[i]=='s' or s[i]=='t' or s[i]=='u' or s[i]=='v' or s[i]=='w' or s[i]=='x' or s[i]=='y' or s[i]=='z':
        count+=1
print('Number of characters appear:',count)

# Input string and count number of uppercase characters.
s=input("Enter a string: ")
count=0
for i in range(0,len(s)):
    if s[i]=='A' or s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='E' or s[i]=='F' or s[i]=='G' or s[i]=='H' or s[i]=='I' or s[i]=='J' or s[i]=='K' or s[i]=='L' or s[i]=='M' or s[i]=='N' or s[i]=='O' or s[i]=='P' or s[i]=='Q' or s[i]=='R' or s[i]=='S' or s[i]=='T' or s[i]=='U' or s[i]=='V' or s[i]=='W' or s[i]=='X' or s[i]=='Y' or s[i]=='Z':
        count+=1
print('Number of characters appear:',count)

# Check if 0 is in string and print number of times 0 appears
int=input("Enter a number: ")
str(int)
count=0
for i in range(len(int)):
    if int[i]=='0':
        count+=1
print('0' in int)
print("Number of times 0 appears:",count)

# Input string and check if palindrome.
s=input("Enter a string: ")
if s==s[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
    
# Input 2 strings, if 2nd string in 1st, print first 4 chars of 2nd string with 'REVERSE' as well
str1=input('Enter string: ')
str2=input('Enter string: ')
if str2 in str1:
    str3=str2[0:4]+'REVERSE'
    print(str3)
else:
    print('')

# Input String and Count Number of Times a Appears
s=input('Enter a string: ')
count=0
for i in range(0,len(s)):
    if s[i]=='a':
        count+=1
print('Number of times \'a\' appear:',count)

# Print Patterns
str='abc'
# 1st Sub Part
for i in range(0,3):
    for j in range(0,i+1):
        print(str[i],end='')
    print()
#2
for i in range(1,4):
    for j in range(0,i):
        print(str[j],end='')
    print()
#3
for i in range(3,0,-1):
    for j in range(0,i):
        print(str[j],end='')
    print()
#4
for i in range(-1,2,1):
    for j in range(2,i,-1):
        print(str[j],end='')
    print()
#5
for i in range(1,4):
    for r in range(1,i+1):
        for j in range(0,i):
            print(str[j],end='')
    print()

# Number of Words in Sentence
s=input('Enter sentence: ')
count=0
for i in range(0,len(s)):
    if s[i]==' ':
        count+=1
print('Number of words in sentence:',(count+1))

# Check if word is in string
s=input('Enter string: ')
w=input('Enter word: ')
if w in s:
    print('Word is in string.')
else:
    print('Word is not in string.')

# Input n names and print Longest Name
n=int(input("Number of names: "))
s=input("Enter name: ")
max=s
for i in range(1,n):
    s=input("Enter name: ")
    while len(s)>len(max):
        max=s
print('Longest name is',max)

# Input n names and print Shortest Name
n=int(input("Number of names: "))
s=input("Enter name: ")
min=s
for i in range(1,n):
    s=input("Enter name: ")
    while len(s)<len(min):
        min=s
print('Shortest name is',min)

# Write a program to enter string and see if all characters are uppercase or lowercase
s=input("Enter a string: ")
if s.upper()==s:
    print('All characters are uppercase.')
elif s.lower()==s:
    print('All characters are lowercase.')
else:
    print('All characters are neither lowercase nor uppercase.')

# Input string and count number of alphabets, numbers and special chars.
s=input("Enter a string: ")
counta,countn,counts=0,0,0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='b' or s[i]=='c' or s[i]=='d' or s[i]=='e' or s[i]=='f' or s[i]=='g' or s[i]=='h' or s[i]=='i' or s[i]=='j' or s[i]=='k' or s[i]=='l' or s[i]=='m' or s[i]=='n' or s[i]=='o' or s[i]=='p' or s[i]=='q' or s[i]=='r' or s[i]=='s' or s[i]=='t' or s[i]=='u' or s[i]=='v' or s[i]=='w' or s[i]=='x' or s[i]=='y' or s[i]=='z' or s[i]=='A' or s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='E' or s[i]=='F' or s[i]=='G' or s[i]=='H' or s[i]=='I' or s[i]=='J' or s[i]=='K' or s[i]=='L' or s[i]=='M' or s[i]=='N' or s[i]=='O' or s[i]=='P' or s[i]=='Q' or s[i]=='R' or s[i]=='S' or s[i]=='T' or s[i]=='U' or s[i]=='V' or s[i]=='W' or s[i]=='X' or s[i]=='Y' or s[i]=='Z':
        counta+=1
    elif '0'<=s[i]<='9':
        countn+=1
    else:
        counts+=1
print('Number of alphabets:',counta)
print('Number of numbers:',countn)
print('Number of special characters:',counts)

# Input string and convert case of string.
n=input('Enter string: ')
if n==n.upper():
    print(n.lower())
elif n==n.lower():
    print(n.upper())
else:
    print('Both upper and lower cases.')

# Input string and count number of letters, uppercase letters, lowercase letters, numbers and special characters.
s=input("Enter a string: ")
counta=countn=counts=countl=countu=0
for i in s:
    if i.isalpha():
        counta+=1
    if i.islower():
        countl+=1
    if i.isupper():
        countu+=1
    if i.isnumeric():
        countn+=1
    if i.isalnum()==False and i.isspace()==False:
        counts+=1
print('Number of lowercase characters:',countl)
print('Number of uppercase characters:',countu)
print('Number of alphabets:',counta)
print('Number of numbers:',countn)
print('Number of special characters:',counts)

# Input string and substring, print number of times substring occurs in string.
## Method 1
s=input('Enter string: ')
ss=input('Enter substring: ')
print('Number of times substring occurs in string:',s.count(ss))
## Method 2
s=input('Enter string: ')
ss=input('Enter substring: ')
count=0
if ss in s:
	count+=1
print('Number of times substring occurs in string:',count)

# Input string containing decimal number and prints out decimal part of number.
s=input('Enter decimal number: ')
print('Decimal part of number: .'+str(s).split(".")[-1])
print("Decimal part of number: ."+s[s.index(".")+1:])

# Input string and capitalise first letter of each word
s=input('Enter string: ')
print('Capitalised string:',s.title())

# Input string, extract numbers and find sum
s=input('Enter string: ')
sum=0
for i in range(0,len(s)):
    if '0'<=s[i]<='9':
        sum+=int(s[i])
print('Sum of all numbers in string:',sum)

# Input string and print each word in new line
s=input('Enter string: ')
s=s.split(' ')
for word in s:
    print(word)

# Input string, capitalise first letter of each word and create new string using that
s=input('Enter string: ')
snew=s.title()
print('Capitalised string:',snew)

# Check if word is in string
s=input('Enter string: ')
w=input('Enter word: ')
if w in s:
    print('Word is in string.')
else:
    print('Word is not in string.')

# Number of times word is in string
s=input('Enter string: ')
w=input('Enter word: ')
print('Number of times word in string:',s.count(w))

# Replace word in string with input word by user
s=input('Enter string: ')
w=input('Enter word for replacing: ')
wn=input('Enter word to replace: ')
s=s.replace(w,wn)
print('New string:',s)

# Input string and word, reverse word and make new text.
s=input('Enter string: ')
w=input('Enter word to replace: ')
wn=w[::-1]
s=s.replace(w,wn)
print('New string:',s)

# Input a string and check if it contains at least one digit or not.
## Method 1
n=input('Enter string: ')
count=0
for i in range(len(n)-1,-1,-1):
    if n[i] in '0123456789':
        count+=1
if count>=1:
    if count==1:
        print('String has one digit.')
    elif count>1:
        print('String has more than one digit.')
else:
    print('String has no digit.')

## Method 2
s=input('Enter string: ')
count=0
for i in range(0,len(s)):
    if '0'<=s[i]<='9':
        count+=1
if count>=1:
    if count==1:
        print('String has one digit.')
    elif count>1:
        print('String has more than one digit.')
else:
    print('String has no digit.')

## Method 3
s=input('Enter string: ')
for i in s:
    if i.isnumeric():
        n=True 
    else:
        n=False
print(n)

# Input string then prints a string that capitalise every other letter in the string
s=input('Enter string: ')
size=True
ns=''
for i in range(0,len(s)):
    if size==True:
        ns+=s[i].capitalize()
        size=False
    else:
        ns+=s[i].lower()
        size=True
print('New string:',ns)

# Input number and convert it to roman numerals
n=int(input("Enter a number: "))
if n>3999:
    print('Run program again and enter another number')
else:
    v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    s=['M','CM','D','CD','D','XD','L','XL','X','IX','V','IV','I']
    r=''
    i=0
    while n>0:
        d=n//v[i]
        n%=v[i]
        while d:
            r+=s[i]
            d-=1
        i+=1
    print('Roman Numeral Form:',r)

# Convert binary number to decimal number
b=input('Enter binary number: ')
dp=b.find('.')
id,fd,twos=0,0,1
for i in range(dp-1,-1,-1):
	id+=((ord(b[i])-ord('0'))*twos)
	twos*=2
twos=2
for i in range(dp+1,len(b)):
    fd+=((ord(b[i])-ord('0'))/twos)
    twos*=2.0
print('Decimal converted number:',id+fd)

# Print toggle case for text given
s='Thursday Is Fun Day'
n=''
for i in range(0,len(s)):
    if s[i].isupper():
        n+=s[i].lower()
    elif s[i].isalpha():
        n+=s[i].upper()
    else:
        n+=' '
print(n)
