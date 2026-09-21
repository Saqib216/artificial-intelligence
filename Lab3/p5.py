# Write a Python program that accepts a word from the user and reverse it.

def reverse_word(word):
    reverse = ""
    for char in word:
        reverse = char + reverse
    return reverse

print(reverse_word(str(input("Enter a word: "))))