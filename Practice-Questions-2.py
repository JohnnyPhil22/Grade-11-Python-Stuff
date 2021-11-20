# Find sum of all odd and even numbers separately
l=eval(input('Enter elements: '))
es,os=0,0
for i in range(0,len(l)):
    if l[i]%2==0:
        es+=l[i]
    else:
        os+=l[i]
print('Sum of even elements:',es,'and sum of odd elements:',os)

# Search for number using linear search
l=eval(input('Enter elements: '))
n=eval(input('Enter number to search: '))
f=False
if n in l:
    f=True
    print('Element is at index number',l.index(n))
else:
    print('Element is not in list')

# Search for number using binary search
def binsrch(l,n,min,max):
    while min<=max:
        mid=min+(max-min)//2
        if l[mid]==n:
            return mid
        elif l[mid]<n:
            min=mid+1
        else:
            max=mid-1
    return -1
l=eval(input('Enter elements: '))
n=eval(input('Enter number to search: '))
r=binsrch(l,n,0,len(l)-1)
if r!=-1:
    print('Element is present at index',str(r))
else:
    print('Element in not in list')

# Reverse list without making new list
l=eval(input('Enter elements: '))
l.reverse()
print('Reversed list:',l)

# Swap first element with second, third with fourth, etc
l=eval(input('Enter elements: '))
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print('Swapped list:',l)

# Swap first half elements to second half
l=eval(input('Enter elements: '))
if len(l)%2!=0:
    print("This program will not accept odd number.")
num=int(len(l)/2)
l1=l[:num]
l2=l[num:]
l.clear()
l.extend(l2)
l.extend(l1)
print("New list:",l)

# All even numbers should be 0 and others 1
l=eval(input('Enter elements: '))
for i in range(0,len(l)):
    if l[i]%2==0:
        l[i]='0'
    else:
        l[i]='1'
print('New list:',l)

# Split list into two one having odd elements and other even
l=eval(input('Enter elements: '))
lodd,leve=[],[]
for i in range(0,len(l)):
    if l[i]%2==0:
        leve.append(l[i])
    else:
        lodd.append(l[i])
print('List with odd elements:',lodd,'and list with even elements:',leve)

# Print prime numbers from list
l=eval(input('Enter elements: '))
p=[]
for i in l:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==1:
        p.append(i)
print('List of prime numbers:',p)

# Print perfect numbers from list
l=eval(input('Enter elements: '))
def isperfect(n):
    if n<1:
        print('Please enter number greater than 1')
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n
print('Perfect numbers:')
for n in range(min(l),(max(l)+1)):
    if isperfect(n):
        print(n)

# Print Armstrong numbers from list
l=eval(input('Enter elements: '))
print('Armstrong numbers:')
for n in range(min(l),max(l)+1):
    o=len(str(n))
    s,t=0,n
    while t>0:
        d=t%10
        s+=d**o
        t//=10
    if n==s:
        print(n)

# Combine two lists of numbers
l1=eval(input('Enter elements for list 1: '))
l2=eval(input('Enter elements for list 2: '))
l=l1+l2
print('Combined list:',l)

# Combine two lists in ascending order (enter first = ascending and second = descending)
a=eval(input('Enter elements for list 1: '))
a.sort()
b=eval(input('Enter elements for list 2: '))
b.sort()
b.reverse()
c=a+b
c.sort()# Print Armstrong numbers from list
print('Combined list:',c)

# Combine two lists alternately
a=[1,5,2,6]
b=[10,6,2,3,7,8,9]
n=min(len(a),len(b))
l=[None]*(n*2)
l[::2]=a[:n]
l[1::2]=b[:n]
l.extend(a[n:])
l.extend(b[n:])
print('New list:',l)

# Sort list using bubble sort
l=eval(input('Enter elements: '))
for j in range(len(l)):
    f=False
    i=0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            f=True
        i+=1
    if f==False:
        break
print('Sorted list:',l)

# Sort list using selection sort
def selsort(l,size):
    for s in range(size):
        min=s
        for i in range(s+1,size):
            if l[i]<l[min]:
                min=i
        l[s],l[min]=l[min],l[s]
l=eval(input('Enter elements: '))
size=len(l)
selsort(l,size)
print('Sorted list:',l)

# Sort list using insertion sort
l=eval(input('Enter elements: '))
for i in range(1,len(l)):
    j=i
    while l[j-1]>l[j] and j>0:
        l[j-1],l[j]=l[j],l[j-1]
        j-=1
print('Sorted list:',l)

# Insert number at given location
l=eval(input('Enter elements: '))
e=eval(input('Enter element to add: '))
p=int(input('Enter index number: '))
l.insert(p,e)
print('New list:',l)

# Delete number from list
l=eval(input('Enter elements: '))
e=eval(input('Enter element to delete: '))
l.remove(e)
print('New list:',l)

# Input m by n matrix and find sum of elements in each row
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
for i in range(r):
    print('Sum of elements in row',i+1,'=',sum(l[i]))

# Input m by n matrix and find sum of elements in each column
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
for i in range(0,c):  
    s=0
    for j in range(0,r):
        s+=l[j][i]
    print('Sum of column',i+1,'=',s)

# Input m by m matrix and print sum of first diagonal
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
s=0
for k in range(r):
    s+=l[k][k]
print('Sum of elements in first diagonal:',s)

# Input m by m matrix and print sum of second diagonal
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
s=0
for k in range(r):
    s+=l[k][k]
print('Sum of elements in second diagonal:',s)

# Input m by m matrix and print lower triangle including first diagonal
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [ ",end="")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Elements in lower triangle:')
for i in range(0,r):
    for j in range(0,c):
        if i<j:
            print(' ',end=' ')
        else:
            print(l[i][j],end=' ')
    print(' ')

# Input m by m matrix and find transpose
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Transposed list: [')
for i in range(c):
    print("\t\t [",end=" ")
    for j in range(r):
        print(l[j][i],end=" ")
    print("]")
print("\t\t ]")

# Append n names to list and search for one name
n=eval(input('Enter names: '))
srchname=input('Enter name to search: ')
if srchname in n:
    print('Name present in list')
else:
    print('Name not present in list')

# Append n names to list and print all names starting with 'a'
n=int(input('Enter number of names: '))
nl=[]
for i in range(n):
    name=input('Enter name '+str(i+1)+': ')
    if name[0]=='a' or name[0]=='A':
        nl.append(name)
print('Names starting with \'a\':',nl)

# Input sentence and print palindrome words
s=input('Enter a string: ')
print('Palindromic words in sentence:')
for w in s.split(' '):
    wn=w.lower()
    if wn==wn[::-1]:
        print(w)

# Replace word in string with input word by user
s=input('Enter string: ')
w=input('Enter word for replacing: ')
wn=input('Enter word to replace: ')
s=s.replace(w,wn)
print('New string:',s)
