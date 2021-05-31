eng=float(input("Enter marks for English: "))
met=float(input("Enter marks for Mathematics: "))
phy=float(input("Enter marks for Physics: "))
che=float(input("Enter marks for Chemistry: "))
com=float(input("Enter marks for Computers: "))
tot=eng+met+phy+che+com
percent=(tot/500)*100
if 91<=percent<=100:
    print("Your percentage is ", percent, ". Your grade is A. You've passed!")
elif 81<=percent<=90:
    print("Your percentage is ", percent, ". Your grade is B. You've passed!")
elif 71<=percent<=80:
    print("Your percentage is ", percent, ". Your grade is C. You've passed!")
elif 61<=percent<=70:
    print("Your percentage is ", percent, ". Your grade is D. You've passed!")
elif percent<=60:
    print("Your percentage is ", percent, ". You've failed!")
