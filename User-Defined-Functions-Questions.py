# Increment elements of list passed as arguments
def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
list1=[10,20,30,40,50]
print('Original list:',list1)
increment(list1)
print('New list:',list1)

# Average of marks
def avgmarks(l,n):
    s=0
    for m in l:
        s+=m
    a=s/n
    return a
l=[]
n=int(input('Enter number of students: '))
for i in range(0,n):
    print('Enter marks of student',(i+1),': ')
    m=int(input())
    l.append(m)
a=avgmarks(l,n)
print('Average of marks:',a)

# If element present in list
l=eval(input('Enter elements for list: '))
def numpreslst(l):
    e=eval(input('Enter element you want to check if in list: '))
    if e in l:
        print('Element is present in list at index number:',l.index(e),'and at position',(l.index(e)+1))
    else:
        print('Element not present in list.')
numpreslst(l)

# Reverse list
l=eval(input('Enter elements of list: '))
def revlist(l):
    return l[-1:-len(l)-1:-1]
print('Reversed list:',revlist(l))

# Remove element by index number or element itself
def delpos(i):
    l.pop(i)
    return l
def delelem(e):
    l.remove(e)
    return l
l=eval(input('Enter list: '))
print('Enter 1 to remove by index number, or 2 to remove by element.')
ch=int(input('Enter choice (1 or 2): '))
if ch==1:
    i=int(input('Enter index number: '))
    print('New list:',delpos(i))
if ch==2:
    e=eval(input('Enter element: '))
    print('New list:',delelem(e))

# Insert element
def insele(l):
    l.insert(i,e)
    return l
l=eval(input('Enter list: '))
e=eval(input('Enter element: '))
i=int(input('Enter index number: '))
print('New list:',insele(l))

# Remove duplicate elements
l=eval(input('Enter elements: '))
def delrepelem(l):
    for i in range(0,len(l)):
        for j in l:
            if l.count(j)>1:
                l.remove(j)
    return l
print('New list:',delrepelem(l))

# Median of List
m=0
def medl(l):
    if len(l)%2==0:
        m=(l[len(l)//2]+l[(len(l)//2)-1])/2
        return m
    else:
        m=l[(len(l)-1)//2]
        return m
l=eval(input('Enter elements: '))
l.sort()
print('Median of list:',medl(l))

# Second largest element
def secmaxno(l):
    l.sort()
    return l[-2]
l=eval(input('Enter elements: '))
print('List given:',l)
l.sort()
print('Second largest element is:',secmaxno(l))

# Largest element
def maxelem(l):
    l.sort()
    return l[-1]
l=eval(input('Enter elements: '))
print('List given:',l)
l.sort()
print('Largest element is:',maxelem(l))

# Frequency of element
def countelem(l,e):
    count=0
    for i in range(0,len(l)):
        if l[i]==e:
            count=count+1
    return count
l=eval(input('Enter elements: '))
e=eval(input('Enter element to count: '))
print('Frequency of element:',countelem(l,e))
