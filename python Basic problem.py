# ==========================================
# 🐍 PYTHON BASICS - PRACTICE CODE
# ==========================================

# 1. Print Hello World
print("Hello, World!")


# 2. Add Two Numbers
a = 10
b = 20
print("Sum:", a + b)


# 3. Even or Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 4. Positive, Negative or Zero
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 5. Largest of Three Numbers
a, b, c = 10, 25, 15
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 6. Print 1 to 10
for i in range(1, 11):
    print(i)


# 7. Sum of 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)


# 8. Multiplication Table
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 9. Factorial
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


# 10. Reverse a Number
num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse:", reverse)


# 11. Sum of Digits
num = 1234
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Digit Sum:", total)


# 12. Check Prime Number
num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# 13. Fibonacci Series
a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()


# 14. Reverse a String
text = "Python"
print("Reverse:", text[::-1])


# 15. Check Palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 16. Count Vowels
text = "Python Programming"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)


# 17. Find Maximum in List
numbers = [10, 40, 20, 90, 50]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Maximum:", largest)


# 18. Find Minimum in List
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Minimum:", smallest)


# 19. Count Even Numbers
numbers = [10, 15, 20, 25, 30, 35]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even Count:", count)


# 20. Find Duplicate Elements
numbers = [10, 20, 10, 30, 20, 40]

for num in set(numbers):
    if numbers.count(num) > 1:
        print("Duplicate:", num)