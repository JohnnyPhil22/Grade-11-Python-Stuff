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
