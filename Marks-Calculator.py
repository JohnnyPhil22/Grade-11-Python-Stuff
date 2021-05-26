eng=input("Enter marks for English: ")
meths=input("Enter marks for Mathematics: ")
sci=input("Enter marks for Science: ")
socsci=input("Enter marks for Social Science: ")
seclang=input("Enter marks for second language (Hindi/French): ")
total=int(eng)+int(meths)+int(sci)+int(socsci)+int(seclang)
percent=(int(total)/500)*100
if percent>=91 and percent<=100:
    print("Your percentage is ", percent, ". Your grade is A1. You've passed successfully!")
elif percent>=81 and percent<=90:
    print("Your percentage is ", percent, ". Your grade is A2. You've passed successfully!")
elif percent>=71 and percent<=80:
    print("Your percentage is ", percent, ". Your grade is B1. You've passed!")
elif percent>=61 and percent<=70:
    print("Your percentage is ", percent, ". Your grade is B2. You've passed!")
elif percent>=51 and percent<=60:
    print("Your percentage is ", percent, ". Your grade is C1. You've nearly passed!")
elif percent>=41 and percent<=50:
    print("Your percentage is ", percent, ". Your grade is C2. You've nearly passed!")
elif percent>=33 and percent<=40:
    print("Your percentage is ", percent, ". Your grade is D. You've passed by the skin of your teeth!")
elif percent>=21 and percent<=32:
    print("Your percentage is ", percent, ". Your grade is E1. You've failed!")
elif percent>=0 and percent<=20:
    print("Your percentage is ", percent, ". Your grade is E2. You've failed!")
