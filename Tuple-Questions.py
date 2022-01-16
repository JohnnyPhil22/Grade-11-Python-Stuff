# Create tuple with single input value
a=eval(input('Enter tuple with one value: '))
print(a)

# Create two tuples from input. First has every 3rd element in reverse order. Second has alternate elements between 3rd and 9th elements.
t=eval(input('Enter elements: '))
t1=t[::-3]
t2=t[3:9:2]
print(t1,'\n',t2)

# Create tuple with 4 elements and unpack to 4 variables. Recreate tuple with 1st element as 3rd and 2nd element as 4th.
t=eval(input('Enter elements: '))
w,x,y,z=t
t=y,z,w,x
print('New tuple:',t)

# Print index of minimum element in tuple
t=eval(input('Enter elements: '))
print('Index of smallest element:',t.index(min(t)))

# Check if it contains all same data type elements
t=eval(input('Enter elements: '))
toe=type(t[0])
for i in range(len(t)):
    if toe==type(t[i]):
        result=True
    else:
        result=False
if result==True:
    print('All elements have same data type')
else:
    print('All elements do not have same data type')

# Create a tuple with student's GR NO, name and marks of 5 subjects. Print name of student, min and max marks.
grno=int(input('Enter GR Number: '))
n=input('Enter name: ')
m1=eval(input('Enter marks for subject 1: '))
m2=eval(input('Enter marks for subject 2: '))
m3=eval(input('Enter marks for subject 3: '))
m4=eval(input('Enter marks for subject 4: '))
m5=eval(input('Enter marks for subject 5: '))
m=m1,m2,m3,m4,m5
t=grno,n,m
print('Name of student:',t[1])
print('Minimum marks:',min(m))
print('Maximum marks:',max(m))

# Linear Search
t=eval(input('Enter elements: '))
n=int(input('Enter element to search: '))
f=False
for i in range(len(t)):
    if t[i]==n:
        f=True
if f==True:
    print('Element found')
else:
    print('Element not found')

# Find frequency of given element
t=eval(input('Enter elements: '))
e=eval(input('Enter element to find frequency: '))
count=0
for i in range(len(t)):
    if t[i]==e:
        count+=1
print('Frequency of element:',count)

# Split tuple into two one having odd and other having even
t=eval(input('Enter elements: '))
l,el,ol=list(t),[],[]
for i in range(len(l)):
    if i%2==0:
        el.append(t[i])
    else:
        ol.append(t[i])
print('Even number tuple:',tuple(el),'and odd number tuple:',tuple(ol))

# Print max and min number from tuple
t=eval(input('Enter elements: '))
print('Maximum number:',max(t),'and minimum number:',min(t))

# Print only names with 5 characters
t=eval(input('Enter elements: '))
print('Names with 5 characters:')
for i in range(len(t)):
    if len(t[i])==5:
        print(t[i])

# Make new tuple with all max values from nested tuples
t=eval(input('Enter elements: '))
l,m=tuple(t),[]
for i in range(len(t)):
    m.append(max(t[i]))
print('Maximum elements:',tuple(m))

# Print tuple of lengths of nested tuples
t=eval(input('Enter elements: '))
l,ntl=list(t),[]
for i in range(len(t)):
    ntl.append(len(t[i]))
print('Lengths of nested tuples:',tuple(ntl))

# Print name and total marks from tuple
t=eval(input('Enter elements: '))
l,nl,ml=list(t),[],[]
for i in range(len(l)):
    nl.append(t[i][0])
    ml.append(t[i][1]+t[i][2])
l.append(tuple(nl))
l.append(tuple(ml))
print(tuple(l[3]+l[4]))

# Print name of student getting highest mark
t=eval(input('Enter elements: '))
l,nl,ml=list(t),[],[]
for i in range(len(l)):
    nl.append(t[i][0])
    ml.append(t[i][1]+t[i][2])
mm=max(ml)
mms=nl.pop(ml.index(mm))
print('Student with maximum marks:',mms)

# Print how many times an element appears in each nested tuple
t=eval(input('Enter elements: '))
e=eval(input('Enter element to count: '))
count=0
for i in range(len(t)):
    for j in range(len(t[i])):
        if e==t[i][j]:
            count+=1
print(e,'appears',count,'times')

# Add mark to a given student
t=eval(input('Enter elements: '))
n=eval(input('Enter student\'s name: '))
m=eval(input('Enter mark of student: '))
for i in range(len(t)):
    if n in t[i]:
        t[i].append(m)
print('New tuple:',t)

# Make new tuple with reversed elements from given tuples
t=eval(input('Enter elements: '))
rt=()
for i in range(len(t)):
    rt=t[::-1]
print('Reversed tuple:',rt)

# Print sum of digits of each number
t=eval(input('Enter elements: '))
nl=[]
for i in range(len(t)):
    n,s=t[i],0
    while n>0:
        a=n%10
        n/=10
        s+=int(a)
    nl.append(s)
print('Tuple of sum of digits:',tuple(nl))

# Input Email of students in list. Create two tuples: one with user name and one with domain.
t=eval(input('Enter elements: '))
ul,dl=[],[]
for i in range(len(t)):
    e=t[i].split('@')
    ul.append(e[0])
    dl.append(e[1])
print('Username tuple:',tuple(ul))
print('Domain name tuple:',tuple(dl))

# Create tuple of n Fibonacci numbers
n=eval(input('Enter number of elements: '))
f1,f2,l=0,1,[]
l.append(f1)
for i in range(1,n):
    l.append(f2)
    next=f1+f2
    f1=f2
    f2=next
print('Tuple of Fibonacci numbers:',tuple(l))

# Count number of pairs in tuple
t=eval(input('Enter elements: '))
count=0
for i in range(len(t)):
    if len(t[i])==2 and (t[i][0]%2==0) and (t[i][1]%2==0):
        count+=1
print('Number of pairs of tuples:',count)

# Print mode from tuple of numbers
t=eval(input('Enter elements: '))
count=0
for i in t:
    if count<t.count(i):
        count=t.count(i)
for i in t:
    if count==t.count(i):
        print('Mode:',i)
        break

# Input nested tuple and print sum of all alternate elements
t=eval(input("Enter elements: "))
l=list(t)
a,s=[],0
for i in t:
    a.extend(i)
for i in range(0,len(a),2):
    s+=a[i]
print("Sum of alternate elements:",s)

# Check if there are multiple maximum elements in tuple
t=eval(input('Enter elements: '))
if t.count(max(t))>1:
    print('There are multiple maximum elements')
else:
    print('There is only one maximum element:',max(t))

# Check if minimum element lies in middle of tuple (odd number of elements)
t=eval(input('Enter elements: '))
if min(t)==t[int(float((len(t))/2)-0.5)]:
    print(min(t),'is middle element')
else:
    print(min(t),'is not middle element')

# Check if elements in tuple are in sorted order or not
t=eval(input('Enter elements: '))
f,i=0,1
while i<len(t):
    if t[i]<t[i-1]:
        f=1
    i+=1
if (not f):
    print('Tuple is sorted')
else:
    print('Tuple is not sorted')
