weight = float(input("Enter weight in KG: "))
height =float(input("Enter height in metres: "))

bmi = weight / (height ** 2)

print("your bmi is:", round(bmi, 2))