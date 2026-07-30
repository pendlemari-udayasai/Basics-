#--------GENERATOR--------

#A generator is a special type of function that produces values one at a time using the yield keyword.
#Unlike normal functions, generators do not return all values at once, which helps save memory.
#Generators are commonly used to process large amounts of data efficiently.
#They can be iterated using a for loop or the next() function


# GENERATORS EXAMPLES

# Example 1: Basic Generator

def numbers():
    yield 1
    yield 2
    yield 3
for i in numbers():
    print(i)


# Example 2: Generator with next()

def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"
g = fruits()
print(next(g))
print(next(g))
print(next(g))


# Example 3: Generate Even Numbers

def even_numbers():
    for i in range(2, 11, 2):
        yield i
for i in even_numbers():
    print(i)


# Example 4: Multiplication Table

def table():
    for i in range(1, 11):
        yield 5 * i
for value in table():
    print(value)

# Example 5: Squares of Numbers

def squares():
    for i in range(1, 6):
        yield i ** 2
for value in squares():
    print(value)


# Example 6: Countdown

def countdown():
    for i in range(5, 0, -1):
        yield i
for value in countdown():
    print(value)


# Example 7: Generate Characters of a String
def characters():
    for ch in "Python":
        yield ch
for letter in characters():
    print(letter)


# Example 8: Cubes of Numbers

def cubes():
    for i in range(1, 6):
        yield i ** 3
for value in cubes():
    print(value)


# Example 9: Generate Odd Numbers

def odd_numbers():
    for i in range(1, 11, 2):
        yield i
for value in odd_numbers():
    print(value)


# Example 10: Fibonacci Series using Generator
def fibonacci():
    a, b = 0, 1
    for i in range(10):
        yield a
        a, b = b, a + b
for value in fibonacci():
    print(value)


# Example 11: Reverse a String using Generator
def reverse(text):
    for i in range(len(text) - 1, -1, -1):
        yield text[i]
for ch in reverse("Python"):
    print(ch)

# Example 12: Generate Numbers from 1 to N
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i
for num in generate_numbers(5):
    print(num)