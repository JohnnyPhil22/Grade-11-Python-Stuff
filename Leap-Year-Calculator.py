x=int(input('Enter the year here:'))
if x==0:
    print('Please enter a proper value')
elif x%4==0 and x%100!=0:
    print(x,'Is a leap year')
elif x%100==0:
    print(x,'Is not a leap year')
elif x%400==0:
    print(x,'Is a leap year')
else:
    print(x,'Is not a leap year')
