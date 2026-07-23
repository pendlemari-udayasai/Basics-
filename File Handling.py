# ==================================
# FILE HANDLING IN PYTHON
# ==================================

# Example 1: Create and Write to a File
file = open("sample.txt", "w")
file.write("Hello, Python!\n")
file.write("Welcome to File Handling.")
file.close()

# Example 2: Read a File
file = open("sample.txt", "r")
print(file.read())
file.close()

# Example 3: Append Data to a File
file = open("sample.txt", "a")
file.write("\nThis line is appended.")
file.close()

# Example 4: Read File Line by Line
file = open("sample.txt", "r")
for line in file:
    print(line.strip())
file.close()


# ==================================
# FILE MODES
# ==================================

# Read Mode (r)
file = open("sample.txt", "r")
print(file.read())
file.close()

# Write Mode (w)
file = open("write.txt", "w")
file.write("Python File Handling")
file.close()

# Append Mode (a)
file = open("write.txt", "a")
file.write("\nLearning Python")
file.close()

# Exclusive Create Mode (x)
# Uncomment to run only once
# file = open("newfile.txt", "x")
# file.close()


# ==================================
# PRACTICE PROGRAMS
# ==================================

# Program 1: Count Characters in a File
file = open("sample.txt", "r")
data = file.read()
print("Characters:", len(data))
file.close()

# Program 2: Count Words in a File
file = open("sample.txt", "r")
data = file.read()
print("Words:", len(data.split()))
file.close()

# Program 3: Count Lines in a File
file = open("sample.txt", "r")
print("Lines:", len(file.readlines()))
file.close()

# Program 4: Copy File Content
source = open("sample.txt", "r")
destination = open("copy.txt", "w")
destination.write(source.read())
source.close()
destination.close()

# Program 5: Check if File Exists
import os

if os.path.exists("sample.txt"):
    print("File Exists")
else:
    print("File Not Found")

# Program 6: Read First Line
file = open("sample.txt", "r")
print(file.readline())
file.close()

# Program 7: Read All Lines into a List
file = open("sample.txt", "r")
print(file.readlines())
file.close()

# Program 8: Delete a File
# Uncomment to run
# import os
# if os.path.exists("copy.txt"):
#     os.remove("copy.txt")
#     print("File Deleted")
# else:
#     print("File Not Found")