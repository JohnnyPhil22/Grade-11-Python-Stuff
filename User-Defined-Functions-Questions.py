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
