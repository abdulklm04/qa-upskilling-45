fruits = ["apple", "banana", "apple"]
fruits.append("mango")
print(fruits)
print(len(fruits))
print("banana" in fruits)

unique = set(fruits)
print(len(unique))

marks = {"Ravi": 80, "Anu": 95}
marks["Kiran"] = 70
print(marks["Anu"])
print(marks.get("Zed", 0))
for name, score in marks.items():
    print(name, score)
