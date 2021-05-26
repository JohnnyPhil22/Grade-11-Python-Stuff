seconds=int(input("Enter time in seconds: "))
number_of_minutes=seconds//60
no_of_minutes_in_seconds=number_of_minutes*60
remaining_seconds=seconds-no_of_minutes_in_seconds
print("The time in minutes and seconds is",number_of_minutes,"minutes and",remaining_seconds,"seconds.")
