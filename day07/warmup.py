class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def greet(self):
        print(f"Hi, I am {self.name}")

    def is_pass(self):
        return self.marks >= 40
s1 = student("Ravi", 80)
s2 = student("Anu", 35)

s1.greet()
print(s1.is_pass())
print(s2.is_pass())
print(s2.name)

class Safe:
    def __init__(self):
        self.__pin = 1234

    def check_pin(self, guess):
        return guess == self.__pin

safe = Safe()
print(safe.check_pin(1234))
print(safe.check_pin(1111))
print(safe.__pin)