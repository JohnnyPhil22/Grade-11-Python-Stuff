# Menu Driven Program for area and circumference of circle & area and perimeter of rectangle.
opt='y'
while opt in 'yY':
    print("1. Area of circle")
    print("2. Circumference of circle")
    print("3. Area of rectangle")
    print("4. Perimeter of rectangle")
    ch=int(input("Enter choice: "))
    if ch==1:
        r=int(input("Enter radius: "))
        print("Area of circle:",(3.14*(r**2)))
    elif ch==2:
        r=int(input("Enter radius: "))
        print("Circumference of circle:",(2*3.14*r))
    elif ch==3:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("Area of rectangle:",(l*b))
    elif ch==4:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("Perimeter of rectangle:",(2*(l+b)))
    else:
        print("Select from options 1 through 4.")
    opt=input("Press y to continue: ")

# Write a menu driven program to perform various list operations.
opt='y'
l=eval(input('Enter elements for list (Enter with [ and ]): '))
while opt in 'yY':
    print('1. Display list')
    print('2. Append an element')
    print('3. Insert an element')
    print('4. Append list to given list')
    print('5. Modify existing element')
    print('6. Delete existing element from position')
    print('7. Delete existing element with given value')
    print('8. Sort list in ascending order')
    print('9. Sort list in descending order')
    ch=int(input('Enter choice: '))
    if ch==1:
        print('List:',l)
    elif ch==2:
        e=eval(input('Enter element: '))
        l.append(e)
    elif ch==3:
        e=eval(input('Enter element: '))
        p=int(input('Enter position: '))
        l.insert(p,e)
    elif ch==4:
        nl=eval(input('Enter list: '))
        l.extend(nl)
    elif ch==5:
        i=int(input('Enter index number: '))
        e=eval(input('Enter element to replace: '))
        del l[i]
        l.insert(i,e)
    elif ch==6:
        i=int(input('Enter index number: '))
        del l[i]
    elif ch==7:
        e=eval(input('Enter element to remove: '))
        l.remove(e)
    elif ch==8:
        l.sort()
    elif ch==9:
        l.sort()
        l.reverse()
    else:
        print("Select from options 1 through 9.")
    opt=input("Press y to continue: ")

# Menu driven program to perform functions on a dictionary
d={}
for i in range(n):
    itemname=input("Input item name: ")
    value=eval(input("The price: "))
    d[itemname]=value
print('''1) To display a particular item price
2) To add new item into dictionary
3) To update an existing item
4) To delete an item
5) Display the dictionary
6) Exit''')
c = int(input("Which option to choose? "))
if c==1:
    item = input("Item to check: ")
    print(d[item])
elif c==2:
    itemn = input("Item to add: ")
    valuen = eval(input("Price to add: "))
    d[itemn]=valuen
    print(d)
elif c==3:
    itemn = input("Item to change: ")
    valuen = eval(input("Price to change: "))
    d[itemn] = valuen
    print(d)
elif c==4:
    itemn = input("Item to delete: ")
    del(d[itemn])
    print(d)
elif c==5:
    print(d)
elif c==6:
    print("Program is done")
else:
    print("Enter proper option")
