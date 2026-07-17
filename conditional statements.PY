#conditional statements

#1. Simple if
num = int(input())
if num > 0:
    print("Positive Number")

#2. if-else
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. if-elif-else
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#nested
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print("Largest =", a)
    else:
        print("Largest =", c)
else:
    if b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)