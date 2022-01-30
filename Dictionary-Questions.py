# Create dictionary with roll number, name and marks of 5 subjects
d={1:19,2:'Jonathan',3:[99,99,99,99,99]}
print(d[2])

# Input the names of students and create dictionary with names as key and value 2500
n=int(input("How many students? "))
t=()
for i in range(n):
    e=eval(input("Student name: "))
    t+=(e,)
d=dict.fromkeys(t,2500)
print(d)

car={'brand':'Ford','model':'Mustang','year':1964}
# Print keys
x=car.keys()
print(x)
# Add another key and value
car['color']='white'
print(x)
# Print items in dictionary
print(car.items())

# Traverse a dictionary
car={'brand':'Ford','model':'Mustang','year':1964}
for i in car:
    print(str(i),':',str(car[i]))

# create a dictionary with roll number, name and computer mark
r=eval(input("Enter roll number: "))
n=eval(input("Enter name: "))
m=eval("Enter Computer marks: "))
d={}
d["Roll Number"]=r
d["Name"]=n
d["CS Mark"]=m
print('Dictionary:',d)

# Create dictionary with n key:value pairs
n=eval(input('Enter number of items: '))
d={}
for i in range(n):
    k=eval(input('Enter key: '))
    v=eval(input('Enter value: '))
    d[k]=v
print('Dictionary:',d)

# Search for value using key in an inputted dictionary
n=eval(input("Enter number of items: "))
d={}
for i in range(n):
    k=eval(input("Enter key: "))
    v=eval(input("Enter value: "))
    d[k]=v
kf=eval(input("Enter value to find: "))
print(d[kf])

# Input sentence and print count of each word
s=eval(input("The sentence: "))
sl=s.split()
d={}
for i in sl:
    d[i]=sl.count(i)
print(d)

# 
