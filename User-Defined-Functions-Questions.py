# Function to increment elements of list passed as arguments
def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
list1=[10,20,30,40,50]
print('Original list:',list1)
increment(list1)
print('New list:',list1)
