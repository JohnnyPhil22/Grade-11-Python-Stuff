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
