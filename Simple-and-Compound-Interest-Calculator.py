P = int(input("Enter principal amount: "))
R = int(input("Enter rate per annum: "))
T = int(input("Enter time of interest: "))
SI = (P*R*T)/100
CI = P * ( 1 +  R / 100)**T
print("The Simple Interest is ",SI,". The Compound Interest is ",CI,".")
