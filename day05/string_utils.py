def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1
    return count

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def capitalize_words(text):
    words = text.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq
        