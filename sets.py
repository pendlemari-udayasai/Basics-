# ===================================
# SETS IN PYTHON
# ===================================

# Example 1: Create a Set
fruits = {"Apple", "Banana", "Mango"}
print(fruits)

# Example 2: Add an Element
fruits.add("Orange")
print(fruits)

# Example 3: Update a Set
fruits.update(["Grapes", "Pineapple"])
print(fruits)

# Example 4: Length of Set
print(len(fruits))



# ===================================
# SET METHODS
# ===================================

# Method 1: remove()
fruits.remove("Banana")
print(fruits)

# Method 2: discard()
fruits.discard("Apple")
print(fruits)

# Method 3: pop()
removed = fruits.pop()
print("Removed:", removed)
print(fruits)

# Method 4: clear()
colors = {"Red", "Blue", "Green"}
colors.clear()
print(colors)

# Method 5: union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# Method 6: intersection()
print(set1.intersection(set2))

# Method 7: difference()
print(set1.difference(set2))

# Method 8: symmetric_difference()
print(set1.symmetric_difference(set2))


# ===================================
# PRACTICE PROGRAMS
# ===================================

# Program 1: Remove Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# Program 2: Check Element Exists
if 3 in set1:
    print("Element Found")
else:
    print("Element Not Found")

# Program 3: Find Maximum Element
print(max(set1))

# Program 4: Find Minimum Element
print(min(set1))

# Program 5: Sum of Elements
print(sum(set1))

# Program 6: Count Total Elements
print(len(set1))

# Program 7: Iterate Through a Set
for item in set1:
    print(item)

# Program 8: Copy a Set
copy_set = set1.copy()
print(copy_set)

# ===================================
# MORE SET PRACTICE PROGRAMS
# ===================================

# Program 9: Create an Empty Set
empty_set = set()
print(empty_set)

# Program 10: Find Common Elements
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.intersection(set2))

# Program 11: Find Unique Elements
print(set1.difference(set2))

# Program 12: Find Symmetric Difference
print(set1.symmetric_difference(set2))

# Program 13: Check if One Set is a Subset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

# Program 14: Check if One Set is a Superset
print(b.issuperset(a))

# Program 15: Check if Two Sets are Disjoint
x = {1, 2}
y = {3, 4}
print(x.isdisjoint(y))

# Program 16: Remove Duplicate Characters from a String
text = "programming"
print(set(text))

# Program 17: Convert Tuple to Set
t = (1, 2, 3, 3, 4, 5)
print(set(t))

# Program 18: Convert List to Set
numbers = [10, 20, 20, 30, 40, 40]
print(set(numbers))

# Program 19: Find Union Using Operator
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)

# Program 20: Find Intersection Using Operator
print(set1 & set2)

# Program 21: Find Difference Using Operator
print(set1 - set2)

# Program 22: Find Symmetric Difference Using Operator
print(set1 ^ set2)

# Program 23: Remove an Element Using discard()
colors = {"Red", "Green", "Blue"}
colors.discard("Green")
print(colors)

# Program 24: Remove an Element Using remove()
colors = {"Red", "Green", "Blue"}
colors.remove("Blue")
print(colors)

# Program 25: Clear All Elements
colors = {"Red", "Green", "Blue"}
colors.clear()
print(colors)

# Program 26: Copy a Set
original = {1, 2, 3}
copied = original.copy()
print(copied)

# Program 27: Iterate Through a Set
languages = {"Python", "Java", "C++"}
for language in languages:
    print(language)

# Program 28: Find Maximum and Minimum Element
numbers = {15, 25, 5, 45, 35}
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Program 29: Sum of Set Elements
print("Sum:", sum(numbers))

# Program 30: Count Elements in a Set
print("Length:", len(numbers))