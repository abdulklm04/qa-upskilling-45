class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old"

    def have_birthday(self):
        self.age = self.age + 1

    def is_adult(self):
        return self.age >= 18