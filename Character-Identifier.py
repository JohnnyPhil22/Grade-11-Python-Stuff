ch=input("Enter only one character: ")
if 'A'<=ch<='Z':
    print("The character is uppercase.")
elif 'a'<=ch<='z':
    print("The character is lowercase.")
elif '0'<=ch<='9':
    print("The character is a digit.")
else:
    print("This is a special character.")
