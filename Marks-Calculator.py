eng=input("Enter marks for English: ")
meths=input("Enter marks for Mathematics: ")
sci=input("Enter marks for Science: ")
socsci=input("Enter marks for Social Science: ")
seclang=input("Enter marks for second language (Hindi/French): ")
total=int(eng)+int(meths)+int(sci)+int(socsci)+int(seclang)
percent=(int(total)/500)*100
print("Your percentage is",percent,".")
