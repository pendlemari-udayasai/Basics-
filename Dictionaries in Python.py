# ==========================
# DICTIONARIES IN PYTHON
# ==========================

# Example 1: Create a Dictionary
student = {
    "name": "Kishore",
    "age": 22,
    "course": "Python"
}
print(student)

# Example 2: Access Dictionary Values
print(student["name"])
print(student["course"])

# Example 3: Add a New Key-Value Pair
student["city"] = "Bangalore"
print(student)

# Example 4: Update a Value
student["age"] = 23
print(student)


# ==========================
# DICTIONARY METHODS
# ==========================

# 1. keys()
print(student.keys())

# 2. values()
print(student.values())

# 3. items()
print(student.items())

# 4. get()
print(student.get("name"))

# 5. update()
student.update({"course": "Full Stack Python"})
print(student)

# 6. pop()
student.pop("city")
print(student)

# 7. clear()
sample = {"a": 1, "b": 2}
sample.clear()
print(sample)


# ==========================
# PRACTICE PROGRAMS
# ==========================

# Program 1: Count Total Keys
student = {
    "name": "Kishore",
    "age": 23,
    "course": "Python"
}
print(len(student))

# Program 2: Print All Keys
for key in student.keys():
    print(key)

# Program 3: Print All Values
for value in student.values():
    print(value)

# Program 4: Print Key-Value Pairs
for key, value in student.items():
    print(key, ":", value)

# Program 5: Check if Key Exists
if "age" in student:
    print("Key Found")
else:
    print("Key Not Found")

# Program 6: Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

# Program 7: Remove Last Item
student.popitem()
print(student)

# Program 8: Copy Dictionary
new_student = student.copy()
print(new_student)

# Program 9: Create Dictionary from Keys
keys = ("id", "name", "course")
value = "Not Assigned"
print(dict.fromkeys(keys, value))

# Program 10: Find Maximum Value
marks = {
    "Math": 90,
    "Science": 95,
    "English": 85
}
print(max(marks.values()))