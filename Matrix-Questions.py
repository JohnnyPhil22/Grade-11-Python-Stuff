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
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t]")

# Create matrix of square 2D list & find sum of elements of first row and diagonals
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
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Sum of elements in first row:',sum(l[0]))
s=0
for k in range(r):
    s+=l[k][k]
print('Sum of elements in diagonals:',s)

# Create 2 matrices & find sum
l1=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
print('---------- LIST 1 ----------')
for i in range(r):
    row1=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row1.append(e) 
    l1.append(row1)
print("2D List created:",l1)
print("3D List: [")
for i in range(r):
    print("\t [",end="")
    for j in range(c):
        print(l1[i][j],end=" ")
    print("]")
print("\t ]")
print('---------- LIST 2 ----------')
l2=[]
for i in range(r):
    row2=[]
    for j in range(c):
        e=int(input("Element at "+str(i)+","+str(j)+": "))
        row2.append(e) 
    l2.append(row2)
print("2D List created:",l2)
print("3D List: [")
for i in range(r):
    print("\t [",end="")
    for j in range(c):
        print(l2[i][j],end=" ")
    print("]")
print("\t ]")
s=[[l1[i][j]+l2[i][j] for j in range(len(l1[0]))] for i in range(len(l1))]
for k in s:
   print(s)

# Write a program to print the elements of upper triangle and lower triangle
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
    print("\t [",end="")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Elements in lower triangle:')
for i in range(0,r):
    for j in range(0,c):
        if i<j:
            print(' ',end=' ')
        else:
            print(l[i][j],end=' ')
    print(' ')
print('Elements in upper triangle:')
for i in range(0,r):
    for j in range(0,c):
        if i>j:
            print(' ',end=' ')
        else:
            print(l[i][j],end=' ')
    print(' ')

# Transpose matrix
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
    print("\t [",end=" ")
    for j in range(c):
        print(l[i][j],end=" ")
    print("]")
print("\t ]")
print('Transposed list: [')
for i in range(c):
    print("\t\t [",end=" ")
    for j in range(r):
        print(l[j][i],end=" ")
    print("]")
print("\t\t ]")
