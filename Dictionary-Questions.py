# Create dictionary with roll number, name and marks of 5 subjects
d={1:19,2:'Jonathan',3:[99,99,99,99,99]}
print(d[2])

# Input the names of students and create dictionary with names as key and value 2500
n=int(input("How many students? "))
t=()
for i in range(n):
    e=eval(input("Student name: "))
    t+=(e,)
d=dict.fromkeys(t,2500)
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

# Input sentence and print count of each word
s=eval(input("The sentence: "))
sl=s.split()
d={}
for i in sl:
    d[i]=sl.count(i)
print(d)

# Highest mark of each student
n=int(input("How many students? "))
d={}
for i in range(n):
    name=eval(input("Input name: "))
    m1=eval(input("Mark 1: "))
    m2=eval(input("Mark 2: "))
    m3=eval(input("Mark 3: "))
    m4=eval(input("Mark 4: "))
    m5=eval(input("Mark 5: "))
    d[name]=[m1,m2,m3,m4,m5]
for i in d:
    print(str(i)+"'s highest mark is "+str(max(d[i])))

# Create a dictionary with n train numbers as key and value is a list of all stops. Print the train numbers which has a stop at Chennai.
n = int(input("How many trains? "))
d = {}
for i in range(n):
    tn = int(input("Input the train number: "))
    ns = int(input("Number of stops: "))
    sl = []
    for j in range(ns):
        stop = input("What is stop "+str(j+1)+"? ")
        sl.append(stop)
    d[tn]=sl
for i in d:
    if "Chennai" in d[i] or "chennai" in d[i] or "CHENNAI" in d[i]:
        print("Train",i,"passes through Chennai")
    else:
        pass
    
# Create a dictionary with n items name as key and value will be a tuple with cp and sp and print the item name with maximum sp and minimum sp
n = int(input("How many items? "))
d = {}
for i in range(n):
    item = input("Input name of item: ")
    cp = eval(input("Cost Price: "))
    sp = eval(input("Selling Price: "))
    d[item] = (cp,sp)
high = 0
highn = ""
for j in d:
    if d[j][1]>high:
        high = d[j][1]
        highn = j
print("Max selling price is:",high)
low = d[item][1]
lown = ""
for k in d:
    if d[k][1]<low:
        low = d[k][1]
        lown = k
print("Min selling price is:",low)

# Create a dictionary with n students name as key and value is a list of 5 marks. Change the dictionary such that the value will be a list in ascending order
Ds = {}
n = int(input("How many students? "))
for i in range(n):
    name = input("The name of student: ")
    m1 = int(input("Marks of Subject 1: "))
    m2 = int(input("Marks of Subject 2: "))
    m3 = int(input("Marks of Subject 3: "))
    m4 = int(input("Marks of Subject 4: "))
    m5 = int(input("Marks of Subject 5: "))
    Ds[name] = sorted([m1,m2,m3,m4,m5])
print(Ds)

# Create a dictionary with exam number as key and value is another dictionary with name, class and gender and print key and values if class is 11.
d = {}
for i in range(n):
    examno = int(input("Exam number: "))
    name = input("Name: ")
    clas = int(input("Class: "))
    gender = input("Gender: ")
    d[examno] = {"Name":name,"Class":clas,"Gender":gender}
for j in d:
    if d[j]["Class"]==11:
        print(str(j)+":"+str(d[j]))
        
# Create a dictionary with key as exam no and value is a dictionary with name, mark which is a list of 5 marks. Print the roll no and name of the student getting rank 1
Ds = {}
n = int(input("How many students? "))
for i in range(n):
    examno = int(input("The exam number of student "+str(i+1)+": "))
    name = input("The name of student "+str(examno)+" : ")
    m1 = int(input("Marks of Sbuject 1: "))
    m2 = int(input("Marks of Sbuject 2: "))
    m3 = int(input("Marks of Sbuject 3: "))
    m4 = int(input("Marks of Sbuject 4: "))
    m5 = int(input("Marks of Sbuject 5: "))
    Ds[examno]=[name,[m1,m2,m3,m4,m5]]
print(Ds)
def avg(l):
    av = sum(l)/len(l)
    return av
high = 0
highn = ""
for k in Ds:
    if avg(Ds[k][1])>high:
        high = avg(Ds[k][1])
        highn = Ds[k][0]
    else:
        pass
print()
print("Highest mark is",high,"held by",highn)

# Voting details should be available in a dictionary in the format key will be roll number and value the name of student voted for and declare the winner.
n = int(input("The number of students: "))
print("Vote for student a or b or c: ")
a = 0
b = 0
c = 0
for i in range(n):
    vote = input("The vote of student "+str(i+1)+": ")
    if vote == "a" or vote == "A":
        a+=1
    elif vote =="b" or vote == "B":
        b+=1
    elif vote == "c" or vote == "C":
        c+=1
    else:
        print("Enter proper vote")
print({"a":a,"b":b,"c":c})
maxv = list({"a":a,"b":b,"c":c}.values())
if max(maxv)==a:
    print("a has the highest number of votes")
elif max(maxv)==b:
    print("b has the highest number of votes")
else:
    print("c has the highest number of votes")

# Create a dictionary with key as name and value is phone number print all your friends’ names who stay in Sharjah assuming the first numbers are 06.
n = int(input("Number of students: "))
d = {}
for i in range(n):
    name = input("Name of student: ")
    phone = input("Phone number: ")
    d[name] = phone
for j in d:
    if d[j][:2]=="06":
        print(j,"lives in sharjah")

# Create a dictionary with e-code as key and value another dictionary with name, date of birth print e-code and names of employees whose birthday falls in a given month.
employees = {}
n = int(input("Number of employees: "))
for i in range(n):
    ecode = int(input("What is the ecode? "))
    name = input("Name of employee: ")
    year = int(input("Year or birth: "))
    mnth = int(input("Month of birth: "))
    day = int(input("Date of birth: "))
    employees[ecode]={"Name":name,"Date of Birth":{"Day":day,"Month":mnth,"Year":year}}
print(employees)
month = int(input("Which month to print? "))
for i in employees:
    if employees[i]["Date of Birth"]["Month"]==month:
        print("Ecode:",i,"Name:",employees[i]["Name"])

# Count the number of times a character occurs in an inputted string
str = input("String: ")
d = {}
for i in str:
    count = str.count(i)
    d[i]=count
print(d)

# Create a dictionary with key as team name and value is a list of number of wins and number of losses
n = int(input("Number of teams: "))
d = {}
for i in range(n):
    name = input("Name: ")
    wins = int(input("Number of wins: "))
    loss = int(input("Number of losses: "))
    d[name] = [wins,loss]
for j in d:
    if d[j][0]>d[j][1]:
        print(j,"has more wins than losses")
    else:
        pass

# Print the names of those students who are eligible for admission
n = int(input("Number of students: "))
d = {}
for i in range(n):
    regno = int(input("Registration number: "))
    name = input("Name: ")
    year = int(input("Year or birth: "))
    mnth = int(input("Month of birth: "))
    day = int(input("Date of birth: "))
    marks = int(input("Total Marks: "))
    d[regno]={"Name":name,"DOB":[day,mnth,year],"Total Marks":marks}
for j in d:
    if (d[j]["Total Marks"]>50) and d[j]["DOB"][2]==2016:
        print(d[j]["Name"],"is elligible")
    else:
        pass

# Perform functions on a dictionary
ODD = {3:"Three",5:"Five",7:"Seven",9:"Nine"}
print("a) ",end="")
k = list(ODD.keys())
for i in k:
    print(i,end=" ")
print()
print("b) ",end="")
v = list(ODD.values())
for i in v:
    print(i,end=" ")
print()
print("c)",ODD)
print("d) The length of the dictionary:",len(ODD))
print("e) ",end="")
if 7 in ODD:
    print("7 is present")
else:
    print("7 is not present")
print("f) ",end="")
if 2 in ODD:
    print("2 is present")
else:
    print("2 is not present")
print("g)",ODD[9])
del(ODD[9])
print("h)",ODD)

# Enter names of employees and their salaries as input and store them
n = int(input("How many employees? "))
d = {}
for i in range(n):
    name = input("What is the name of the employee? ")
    salary = int(input("What is "+name+"'s salary? "))
    d[name] = salary
print(d)

# Find the highest 2 values in a dictionary
n = int(input("Number of items: "))
d = {}
for i in range(n):
    key = input("The key: ")
    value = eval(input("The value: "))
    d[key] = value
x = list(d.values())
x.sort()
print(x[-1])
print(x[-2])

# Perform functions on a phonebook
n = int(input("Number of friends: "))
pbk = {}
for i in range(n):
    name = input("Name of friend: ")
    phone = int(input("Phone number of "+name+": "))
    pbk[name]=phone
print()
print("a)",pbk)
print()
print("b)",end=" ")
namen = input("New name to add: ")
phonen = int(input("Phone number of "+namen+": "))
pbk[namen]=phonen
print(pbk)
print()
print("c)",end=" ")
named = input("Friend to delete: ")
del(pbk[named])
print(pbk)
print()
print("d)",end=" ")
namec = input("Which person's number to change: ")
phonec = int(input("Changed phone number: "))
pbk[namec] = phonec
print(pbk)
print()
print("e)",end=" ")
namech = input("Which person to check in the dictionary: ")
if namech in pbk:
    print(namech,"is in the phonebook")
else:
    print(namech,"is not in the phonebook")
print()
print("f)",end=" ")
x = list(pbk.keys())
x.sort()
pbk2 = {}
for i in x:
    pbk2[i]=pbk[i]
print(pbk2)
