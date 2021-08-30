# Input a string and count number of times 'a', 'A' appear in the sentence.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='A':
        count+=1
print('Number of times \'a\' or \'A\' appear:',count)

# Input string and count number of vowels.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
       count+=1
print('Number of times vowels appear:',count)

# Input tring and count number of consonants.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    if s[i]!='a' or s[i]!='A' or s[i]!='e' or s[i]!='E' or s[i]!='i' or s[i]!='I' or s[i]!='o' or s[i]!='O' or s[i]!='u' or s[i]!='U':
        count+=1
print('Number of times consonants appear:',count)

# Input string and count number of characters.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    count+=1
print('Number of characters appear:',count)

# Input string and count number of lowercase characters.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    if s[i]=='a' or s[i]=='b' or s[i]=='c' or s[i]=='d' or s[i]=='e' or s[i]=='f' or s[i]=='g' or s[i]=='h' or s[i]=='i' or s[i]=='j' or s[i]=='k' or s[i]=='l' or s[i]=='m' or s[i]=='n' or s[i]=='o' or s[i]=='p' or s[i]=='q' or s[i]=='r' or s[i]=='s' or s[i]=='t' or s[i]=='u' or s[i]=='v' or s[i]=='w' or s[i]=='x' or s[i]=='y' or s[i]=='z':
        count+=1
print('Number of characters appear:',count)

# Input string and count number of uppercase characters.
s=input("Enter anything: ")
count=0
for i in range(0,len(s)):
    if s[i]=='A' or s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='E' or s[i]=='F' or s[i]=='G' or s[i]=='H' or s[i]=='I' or s[i]=='J' or s[i]=='K' or s[i]=='L' or s[i]=='M' or s[i]=='N' or s[i]=='O' or s[i]=='P' or s[i]=='Q' or s[i]=='R' or s[i]=='S' or s[i]=='T' or s[i]=='U' or s[i]=='V' or s[i]=='W' or s[i]=='X' or s[i]=='Y' or s[i]=='Z':
        count+=1
print('Number of characters appear:',count)

# Input string and check if palindrome.
s=input("Enter a string: ")
if s==s[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
