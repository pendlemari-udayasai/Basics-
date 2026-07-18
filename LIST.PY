#---------
#List
#----------
#A list is an ordered and mutable collection used to store multiple items in a single variable.
#Lists can contain different data types such as integers, strings, and floating-point values.
#Elements in a list are accessed using their index, starting from 0.
#Lists allow adding, removing, updating, and organizing data efficiently.
#------------
#list methods
#------------
#List methods are built-in functions used to perform operations on lists.
#They help add, remove, sort, search, and modify list elements easily.
#Common methods include append(), insert(), remove(), pop(), sort(), and reverse().
#List methods make data management simple, flexible, and efficient.

# ==========================
# LISTS IN PYTHON
# ==========================

# Example 1: Create a List
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Example 2: Access List Elements
print(fruits[0])
print(fruits[-1])

# Example 3: List Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# Example 4: Update List
fruits[1] = "Orange"
print(fruits)
# ==========================
# LIST METHODS
# ==========================
# 1. append()
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

# 2. insert()
fruits.insert(1, "Orange")
print(fruits)

# 3. remove()
fruits.remove("Banana")
print(fruits)

# 4. pop()
fruits.pop()
print(fruits)

# 5. sort()
numbers = [50, 20, 10, 40, 30]
numbers.sort()
print(numbers)

# 6. reverse()
numbers.reverse()
print(numbers)

# 7. count()
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

# 8. index()
fruits = ["Apple", "Orange", "Mango"]
print(fruits.index("Mango"))

# ==========================
# PRACTICE PROGRAMS
# ==========================

# Program 1: Find Largest Number
numbers = [10, 40, 25, 90, 15]
print(max(numbers))

# Program 2: Find Smallest Number
print(min(numbers))

# Program 3: Sum of List Elements
print(sum(numbers))

# Program 4: Count Total Elements
print(len(numbers))

# Program 5: Check Element Exists
if 25 in numbers:
    print("Found")
else:
    print("Not Found")

# Program 6: Print All Elements
for i in numbers:
    print(i)

# Program 7: Remove Duplicates
nums = [1, 2, 2, 3, 4, 4]
print(list(set(nums)))

# Program 8: Reverse a List
numbers.reverse()
print(numbers)