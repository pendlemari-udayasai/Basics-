# ==========================================================
#              PRIME NUMBERS - 20 PROGRAMS
# ==========================================================

# 1. Check whether a number is Prime
num = 17

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("1. Not Prime")
            break
    else:
        print("1. Prime")
else:
    print("1. Not Prime")


# 2. Print Prime Numbers from 1 to 100
print("2. Primes from 1 to 100:")
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()


# 3. Print Prime Numbers between Two Numbers
start, end = 20, 50

print("3. Primes between 20 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()


# 4. Count Prime Numbers from 1 to 100
count = 0

for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1

print("4. Prime Count:", count)


# 5. Sum of Prime Numbers from 1 to 100
total = 0

for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        total += num

print("5. Prime Sum:", total)


# 6. Largest Prime Below a Number
num = 50

for n in range(num - 1, 1, -1):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print("6. Largest Prime:", n)
        break


# 7. Smallest Prime Above a Number
num = 50
n = num + 1

while True:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print("7. Smallest Prime:", n)
        break
    n += 1


# 8. First 10 Prime Numbers
primes = []
num = 2

while len(primes) < 10:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print("8. First 10 Primes:", primes)


# 9. First N Prime Numbers
N = 15
primes = []
num = 2

while len(primes) < N:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print("9. First", N, "Primes:", primes)


# 10. Find Nth Prime Number
N = 10
count = 0
num = 2

while count < N:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1
        if count == N:
            print("10. Nth Prime:", num)
            break
    num += 1


# 11. Find Prime Numbers in a List
numbers = [10, 11, 13, 15, 17, 20, 23]
primes = []

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("11. Primes in List:", primes)


# 12. Count Prime Numbers in a List
numbers = [2, 4, 5, 8, 11, 13, 15]
count = 0

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1

print("12. Prime Count:", count)


# 13. Sum of Prime Numbers in a List
numbers = [2, 4, 5, 8, 11, 13]
total = 0

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            total += num

print("13. Prime Sum:", total)


# 14. Largest Prime in a List
numbers = [10, 17, 5, 23, 8, 29, 12]
prime_list = []

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_list.append(num)

print("14. Largest Prime:", max(prime_list))


# 15. Smallest Prime in a List
numbers = [10, 17, 5, 23, 8, 29, 12]
prime_list = []

for num in numbers:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_list.append(num)

print("15. Smallest Prime:", min(prime_list))


# 16. Find Prime Factors
num = 60
original = num
factors = []

for i in range(2, num + 1):
    while num % i == 0:
        factors.append(i)
        num //= i

print("16. Prime Factors of", original, ":", factors)


# 17. Count Prime Factors
num = 60
count = 0

for i in range(2, num + 1):
    while num % i == 0:
        count += 1
        num //= i

print("17. Number of Prime Factors:", count)


# 18. Check Whether Two Numbers are Prime
a, b = 17, 23

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

if is_prime(a) and is_prime(b):
    print("18. Both Numbers are Prime")
else:
    print("18. Both are not Prime")


# 19. Check Whether Sum of Two Numbers is Prime
a, b = 10, 7
result = a + b

if is_prime(result):
    print("19. Sum is Prime:", result)
else:
    print("19. Sum is Not Prime:", result)


# 20. Find Two Prime Numbers Whose Sum Equals Given Number
target = 10

for a in range(2, target):
    b = target - a

    if is_prime(a) and is_prime(b):
        print("20.", a, "+", b, "=", target)
        break