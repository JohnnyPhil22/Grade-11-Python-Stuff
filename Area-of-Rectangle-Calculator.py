l = input("Enter Length: ")
b = input("Enter Breadth: ")
Ar = int(l) * int(b)
if l == b:
    print("The area of the square is", Ar, "unit squared.")
if l != b:
    print("The area of the rectangle is", Ar, "unit squared.")
