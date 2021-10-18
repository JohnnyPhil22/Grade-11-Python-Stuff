# Basic matrix creator
l=[]
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input('Element at '+str(i)+','+str(j)+': '))
        row.append(e) 
    l.append(row)
print("list created is:",l)
print("lst=[")
for i in range(r):
    print("\t",end="")
    for j in range(c):
        print(l[i][j],end="")
    print("]")
