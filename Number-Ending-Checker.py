no = int(input("Enter a number: "))
if no%10==4:
    print("Ends with 4.")
else:
    if no%10==8:
        print("Ends with 8.")
    else:
        print("Ends with neither.")
