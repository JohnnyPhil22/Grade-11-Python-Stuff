a = int(input("Enter coefficient for first term in quadratic equation: "))
b = int(input("Enter coefficient for second term in quadratic equation: "))
c = int(input("Enter coefficient for third term in quadratic equation: "))

d = (b**2)-(4*a*c)

sol1 = (-b-(d**0.5))/(2*a)
sol2 = (-b+(d**0.5))/(2*a)

print("The solutions are",sol1,"and",sol2,".")
