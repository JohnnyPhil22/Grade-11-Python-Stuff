# Write a program to create nested list with 10 elements where 4th element is nested list with 4 elements. Access all elements with indexing.
list1=[0,0,7,['J','P',2,2],9,9,5,'l','s','t']
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[3][0])
print(list1[3][1])
print(list1[3][2])
print(list1[3][3])
print(list1[4])
print(list1[5])
print(list1[6])
print(list1[7])
print(list1[8])
print(list1[9])

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
