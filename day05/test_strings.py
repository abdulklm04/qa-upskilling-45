from string_utils import reverse_string, count_vowels, is_anagram, capitalize_words, char_frequency

print(reverse_string("hello"))
print(reverse_string("QA"))
print(reverse_string(""))

print(count_vowels("hello"))
print(count_vowels("QA Tester"))
print(count_vowels("rhythm"))
print(count_vowels(""))

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("Race", "care"))
print(is_anagram("abc", "ab"))

print(capitalize_words("hello qa world"))
print(capitalize_words("python"))
print(capitalize_words("  many   spaces  here "))
print(capitalize_words(""))

print(char_frequency("hello"))
print(char_frequency("aab"))
print(char_frequency(""))
