# Create 2D and 3D list
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List=[")
for i in range(r):
    print("\t[ ",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t]")

# Create matrix of 2 by 3 2D list & find sum of elements of first row and diagonals
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row.append(e) 
    l.append(row)
print("2D List created:",l)
print("3D List: [")
for i in range(r):
    print("\t [ ",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Sum of elements in first row:',sum(l[0]))
s=(l[0][0])+(l[1][2])
print('Sum of elements in diagonals:',s)
