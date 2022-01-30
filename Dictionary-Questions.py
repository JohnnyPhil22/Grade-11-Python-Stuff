# Create dictionary with roll number, name and marks of 5 subjects
d={1:19,2:'Jonathan',3:[99,99,99,99,99]}
print(d[2])

# Your school has decided to give an scholarship amount of AED 2500 to few students. Input names of students in list or tuple and create dictionary with name as key and value as 2500.
d={'names':['Jonathan','John'],'value':2500}
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
