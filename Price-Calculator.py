no=int(input("Enter number of items: "))
if no<10:
    price=120*no
    print("Total amount:",price)
elif 10<=no<=99:
    price=100*no
    print("Total amount:",price)
elif no>=100:
    price=70*no
    print("Total amount:",price)
