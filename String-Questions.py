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

# 3number of Words in Sentence
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
