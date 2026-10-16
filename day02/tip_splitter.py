bill = float(input("What is the bill Amount:"))
tip_percent = float(input("What is the tip percentage:" ))
people = int(input("How many person:"))

tip = bill * tip_percent/100
total = bill + tip
per_person = total / people

print("Total tip:", tip)

print("Tip + Total:", total)

print("Amount per person:", round(per_person, 2))