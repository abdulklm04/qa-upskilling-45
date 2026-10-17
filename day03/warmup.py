number = int(input("Enter a number:" ))
if number % 2 == 0:
    print("Even")
else:
    print("odd")

for i in range(1, 6):
    print(i)

count = 3
while count > 0:
    print(count)
    count = count - 1
print("Go!")

for row in range(1, 4):
    for col in range (1, 4):
        print(row * col, end=" ")
    print()
    