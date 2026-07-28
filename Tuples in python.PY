# ===================================
# TUPLES IN PYTHON
# ===================================

# Example 1: Create a Tuple
fruits = ("Apple", "Banana", "Mango")
print(fruits)

# Example 2: Access Tuple Elements
print(fruits[0])      # First element
print(fruits[-1])     # Last element

# Example 3: Tuple Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# Example 4: Length of Tuple
print(len(numbers))


# ===================================
# TUPLE METHODS
# ===================================

# Method 1: count()
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# Method 2: index()
fruits = ("Apple", "Banana", "Mango")
print(fruits.index("Banana"))


# ===================================
# PRACTICE PROGRAMS
# ===================================

# Program 1: Find Maximum Element
numbers = (10, 40, 25, 90, 15)
print(max(numbers))

# Program 2: Find Minimum Element
print(min(numbers))

# Program 3: Sum of Tuple Elements
print(sum(numbers))

# Program 4: Count Total Elements
print(len(numbers))

# Program 5: Check Element Exists
if 25 in numbers:
    print("Element Found")
else:
    print("Element Not Found")

# Program 6: Iterate Through Tuple
for i in numbers:
    print(i)

# Program 7: Concatenate Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# Program 8: Repeat Tuple
colors = ("Red", "Blue")
print(colors * 3)d