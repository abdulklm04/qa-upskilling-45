def is_even(number):
    return number % 2 == 0

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def reverse_string(text):
    return text[::-1]

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def calculate_intrest(principle, rate, time):
    return (principle * rate * time) / 100

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
