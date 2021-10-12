# Create nested list with 10 elements where 4th element is nested list with 4 elements. Access all elements with indexing.
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
list1=['J','P',2,2]
list2=['_',0,0,7]
print(list1+list2)

# Traverse a list.
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

# Print elements of list in separate lines along with element's both indexes.
list1=['q','w','e','r','t','y']
for a in range(len(list1)):
    print('At indexes',a,'and',(a-len(list1)),'element present:',list1[a])

# Take two lists with elements as numbers from 1 to 20. Find sum of elements between indexes 5 to 15 in first list. Find average of every fourth element in second list.
l1=l2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l1new=l1[6:15:2]
l2new=l2[::4]
s1=s2=count=0
print('New first list:',l1new)
for i in l1new:
    s1+=i
print('Sum of elements between indexes 5 to 15 in first list:',s1)
print('New second list:',l2new)
for j in l2new:
    s2+=j
    count+=1
s2=s2/count
print('Average of every fourth element in second list:',s2)

# Make copy of list with 10 elements then add 10 to first and last element of copied list.
l1=[1,2,3,4,5,6,7,8,9,10]
l2=l1.copy()
l2[0]+=10
l2[9]+=10
print(l1,l2)

# Take input of elements from users and give smallest number and it's index.
## Method 1
l=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(l)):
    m=min(l)
print('The smallest element is',m,'and it\'s index number is',l.index(m))
## Method 2
l=eval(input('Enter elements: '))
print('List given:',l)
print('Smallest element is',min(l),'and it\'s index number is',l.index(min(l)))
## Method 3
l=list(input('Enter elements: '))
print(l)
print('Smallest element is',min(l),'and it\'s index number is',l.index(min(l)))
