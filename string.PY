#A string is a sequence of characters enclosed in single (' '), double (" "), or triple (''' ''') quotes.
#Strings are used to store and manipulate text data in Python.
#They support operations like indexing, slicing, and concatenation.
#Strings are immutable, which means their characters cannot be changed after creation.##

#---String Methods---
#*String methods are built-in functions used to perform operations on strings.
#*They help modify, search, split, replace, and format text efficiently.
#*Common methods include upper(), lower(), replace(), split(), and strip().
#*String methods make text processing simpler, faster, and more readable.

# ==========================
# STRINGS IN PYTHON
# ==========================
# Example 1: Create a String
text = "Python Programming"
print(text)
# Example 2: Access Characters
text = "Python"
print(text[0])
print(text[-1])
# Example 3: String Slicing
text = "Python Programming"
print(text[0:6])
print(text[7:])
print(text[::-1])
# Example 4: String Length
text = "Python"
print(len(text))

# ==========================
# STRING METHODS
# ==========================
# 1. upper()
text = "python"
print(text.upper())
# 2. lower()
text = "PYTHON"
print(text.lower())

# 3. capitalize()
text = "python programming"
print(text.capitalize())

# 4. title()
text = "python programming language"
print(text.title())

# 5. strip()
text = "   Python   "
print(text.strip())

# 6. replace()
text = "I like Java"
print(text.replace("Java", "Python"))

# 7. find()
text = "Python Programming"
print(text.find("Program"))

# 8. count()
text = "banana"
print(text.count("a"))

# 9. startswith()
text = "Python Programming"
print(text.startswith("Python"))

# 10. endswith()
text = "Python Programming"
print(text.endswith("ing"))

# 11. split()
text = "Python,Java,C++"
print(text.split(","))

# 12. join()
languages = ["Python", "Java", "C++"]
print(" | ".join(languages))

# ==========================
# PRACTICE PROGRAMS
# ==========================

# Program 1: Reverse a String
text = "Python"
print(text[::-1])

# Program 2: Check Palindrome
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Program 3: Count Vowels
text = "Programming"
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels =", count)

# Program 4: Count Words
text = "Python is easy to learn"
words = text.split()
print("Total Words =", len(words))

# Program 5: Remove Spaces
text = "Python Programming"
print(text.replace(" ", ""))

# Program 6: Count Characters
text = "Python"
print("Characters =", len(text))

# Program 7: Check String Starts with 'P'
text = "Python"
if text.startswith("P"):
    print("Starts with P")
else:
    print("Does not start with P")

# Program 8: Convert to Uppercase
text = "python programming"
print(text.upper())

# Program 9: Convert to Lowercase
text = "PYTHON PROGRAMMING"
print(text.lower())

# Program 10: Replace a Word
text = "I love Java"
print(text.replace("Java", "Python"))