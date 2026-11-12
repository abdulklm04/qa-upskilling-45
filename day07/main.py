from person import person
from bank_account import BankAccount

p1 = person("Ravi", 25)
p2 = person("Anu", 30)

print(p1.introduce())
print(p2.introduce())
print(p1.name)

p1.have_birthday()
print(p1.age)
print(p1.is_adult())
print(person("Kid", 10).is_adult())

account = BankAccount("Ravi", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.get_balance())
print(account.withdraw(200))
print(account.get_balance())
print(account.withdraw(5000))
print(account.get_balance())
print(account.deposit(-50))
print(account.get_balance())

account._balance = 999999
print(account.get_balance())