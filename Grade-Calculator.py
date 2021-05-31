eng=input("Enter marks for English: ")
met=input("Enter marks for Mathematics: ")
phy=input("Enter marks for Physics: ")
che=input("Enter marks for Chemistry: ")
com=input("Enter marks for Computers: ")
total=float(eng)+float(met)+float(phy)+float(che)+float(com)
percent=(int(total)/500)*100
if percent>=91 and percent<=100:
    print("Your percentage is ", percent, ". Your grade is A. You've passed!")
elif percent>=81 and percent<=90:
    print("Your percentage is ", percent, ". Your grade is B. You've passed!")
elif percent>=71 and percent<=80:
    print("Your percentage is ", percent, ". Your grade is C. You've passed!")
elif percent>=61 and percent<=70:
    print("Your percentage is ", percent, ". Your grade is D. You've passed!")
elif percent<=60:
    print("Your percentage is ", percent, ". You've failed!")
