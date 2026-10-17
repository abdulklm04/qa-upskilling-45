word = input("Enter a word: ")
word = word.lower()
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
    print("Reversed word:", reversed_word)