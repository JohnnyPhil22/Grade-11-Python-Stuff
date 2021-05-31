eng=input("Enter marks for English: ")
meths=input("Enter marks for Mathematics: ")
sci=input("Enter marks for Science: ")
socsci=input("Enter marks for Social Science: ")
seclang=input("Enter marks for second language (Hindi/French): ")
total=int(eng)+int(meths)+int(sci)+int(socsci)+int(seclang)
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
