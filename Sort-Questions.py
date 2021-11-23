# Linear Search
l=[4,2,8,9,3,7]
x=int(input('Enter number to search: '))
f=False
for i in range(len(l)):
    if l[i]==x:
        f=True
        break
if f==False:
    print(x,'is not in list')
else:
    print(x,'found at position',(i+1))

# Bubble Sort
## Method 1
l=[6,19,1,15,11,12,14]
for j in range(len(l)):
    s=False
    i=0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            s=True
        i+=1
    if s==False:
        break
print('Sorted list:',l)
## Method 2
l=[15,6,13,22,3,52,2]
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print('Sorted list:',l)

# Selection Sort
def selsort(l,s):
    for step in range(s):
        min=step
        for i in range(step+1,s):
            if l[i]<l[min]:
                min=i
        l[step],l[min]=l[min],l[step]
l=eval(input('Enter elements: '))
s=len(l)
selsort(l,s)
print('Sorted list:',l)

# Insertion sort
## Method 1
s=int(input('Enter size of list: '))
l=[]
for i in range(s):
    e=int(input('Enter element '+str(i+1)+': '))
    l.append(e)
for i in range(1,s):
    t=l[i]
    j=i-1
    while j>=0 and t<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=t
print('Sorted list:',l)
## Method 2
def inssort(l):
    for i in range(1,len(l)):
        j=i
        while l[j-1]>l[j] and j>0:
            l[j-1],l[j]=l[j],l[j-1]
            j-=1
l=[2,6,5,1,3,4]
inssort(l)
print('Sorted list:',l)
