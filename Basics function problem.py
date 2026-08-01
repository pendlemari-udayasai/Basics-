# ==========================================
# 25 BASIC PYTHON FUNCTION PROGRAMS
# ==========================================

# 1. Print Hello
def hello():
    print("Hello, Python!")
hello()

# 2. Add Two Numbers
def add(a, b):
    return a + b
print(add(10, 20))

# 3. Subtract Two Numbers
def subtract(a, b):
    return a - b
print(subtract(20, 5))

# 4. Multiply Two Numbers
def multiply(a, b):
    return a * b
print(multiply(5, 4))

# 5. Divide Two Numbers
def divide(a, b):
    return a / b
print(divide(20, 5))

# 6. Square of a Number
def square(n):
    return n ** 2
print(square(6))

# 7. Cube of a Number
def cube(n):
    return n ** 3
print(cube(3))

# 8. Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"
print(even_odd(7))

# 9. Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    return b
print(largest(10, 20))

# 10. Largest of Three Numbers
def largest3(a, b, c):
    return max(a, b, c)
print(largest3(10, 30, 20))

# 11. Positive, Negative or Zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
print(check_number(-5))

# 12. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(factorial(5))

# 13. Prime Number
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime(13))

# 14. Reverse String
def reverse(text):
    return text[::-1]
print(reverse("Python"))

# 15. Palindrome
def palindrome(text):
    return text == text[::-1]
print(palindrome("madam"))

# 16. Sum of List
def list_sum(lst):
    return sum(lst)
print(list_sum([10, 20, 30]))

# 17. Average of List
def average(lst):
    return sum(lst) / len(lst)
print(average([10, 20, 30]))

# 18. Count Vowels
def vowels(text):
    count = 0
    for i in text.lower():
        if i in "aeiou":
            count += 1
    return count
print(vowels("Programming"))

# 19. Count Digits
def count_digits(n):
    return len(str(n))
print(count_digits(12345))

# 20. Sum of Digits
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(sum_digits(1234))

# 21. Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
print()
fibonacci(10)

# 22. Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
table(5)

# 23. Minimum of Three Numbers
def minimum(a, b, c):
    return min(a, b, c)
print(minimum(10, 5, 20))

# 24. Swap Two Numbers
def swap(a, b):
    a, b = b, a
    return a, b
print(swap(10, 20))

# 25. Calculator
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid Operator"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))