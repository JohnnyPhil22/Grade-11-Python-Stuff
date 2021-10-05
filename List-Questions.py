# Write a program to create nested list with 10 elements where 4th element is nested list with 4 elements. Access all elements with indexing.

# Create two lists and concatenate them.

# Write a program to traverse a list.
list1=['Red','Green','Blue','Yellow','Black']
## For loop
### Method 1
for i in list1:
    print(i)
### Method 2
for i in range(len(list1)):
    print(list1[i])
## While loop
i=0
while i<len(list1):
    print(list1[i])
    i+=1

# Write program to print elements of list in separate lines along with element's both indexes.
list1=['q','w','e','r','t','y']
for a in range(len(list1)):
    print('At indexes',a,'and',(a-len(list1)),'element present:',list1[a])
