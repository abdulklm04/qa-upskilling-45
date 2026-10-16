principal = float(input("What is the Principal amount:" ))
rate = float(input("Rate of intrest:" ))
time = float(input("No of years:" ))

intrest = (principal * rate * time) / 100

print("Your Intrest amount is:", intrest)
print("Total amount is:", principal + intrest)