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
