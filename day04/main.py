from utils import is_even, max_of_three, reverse_string, calculate_bmi, calculate_intrest, factorial, is_prime

number = int(input("Enter a number: "))

if is_even(number):
    print("even")
else:
    print("odd")

print(max_of_three(10, 2, 4))
print(max_of_three(1, 1, 1))
print(max_of_three(-5, -2, -9))
print(max_of_three(3, 9, 5))

print(reverse_string("hello"))

print(calculate_bmi(70, 1.75))

print(calculate_intrest(10000, 5, 2))

print(factorial(5))
print(factorial(0))

print(is_prime(7))
print(is_prime(10))
print(is_prime(2))
print(is_prime(1))  