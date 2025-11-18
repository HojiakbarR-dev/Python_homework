# ================================
# 1) Modify String with Underscores
# ================================
def modify_with_underscores(s):
    vowels = set("aeiouAEIOU")
    res = []
    count = 0
    i = 0

    while i < len(s):
        res.append(s[i])
        count += 1

        if count == 3:
            pos = i  # position where underscore should go

            while pos < len(s) - 1 and s[pos] in vowels:
                pos += 1

            if pos < len(s) - 1:
                res.append("_")
                count = 0
            else:
                count = 0

        i += 1

    if res and res[-1] == "_":
        res.pop()

    return "".join(res)


print("Task 1 Outputs:")
print(modify_with_underscores("hello"))
print(modify_with_underscores("assalom"))
print(modify_with_underscores("abcabcabcdeabcdefabcdefg"))
print()


# ================================
# 2) Integer Squares Exercise
# ================================
print("Task 2 Output:")
n = 5
for i in range(n):
    print(i * i)
print()


# ================================
# 3) LOOP EXERCISES
# ================================

# Exercise 1: Print first 10 natural numbers
print("Exercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2: Pattern
print("Exercise 2:")
for r in range(1, 6):
    for c in range(1, r+1):
        print(c, end=' ')
    print()
print()

# Exercise 3: Sum 1 to n
print("Exercise 3:")
n = 10
total = n * (n + 1) // 2
print("Sum is:", total)
print()

# Exercise 4: Multiplication table
print("Exercise 4:")
num = 2
for i in range(1, 11):
    print(num * i)
print()

# Exercise 5: Display numbers from a list
print("Exercise 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if 50 < n < 500 and n % 5 == 0 and n % 10 != 0:
        print(n)
print()

# Exercise 6: Count digits
print("Exercise 6:")
num = "75869"
print(len(num))
print()

# Exercise 7: Reverse number pattern
print("Exercise 7:")
n = 5
for start in range(n, 0, -1):
    for x in range(start, 0, -1):
        print(x, end=' ')
    print()
print()

# Exercise 8: Reverse list
print("Exercise 8:")
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
print()

# Exercise 9: -10 to -1
print("Exercise 9:")
for i in range(-10, 0):
    print(i)
print()

# Exercise 10: Done message
print("Exercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")
print()

# Exercise 11: Primes in range
print("Exercise 11:")

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

a, b = 25, 50
for num in range(a, b+1):
    if is_prime(num):
        print(num)
print()

# Exercise 12: Fibonacci
print("Exercise 12:")
terms = 10
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# Exercise 13: Factorial
print("Exercise 13:")
n = 5
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! =", fact)
print()


# ================================
# 4) Uncommon Elements of Lists
# ================================
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    all_keys = set(c1.keys()) | set(c2.keys())

    for key in all_keys:
        diff = c1[key] - c2[key]
        if diff > 0:
            result.extend([key] * diff)
        elif diff < 0:
            result.extend([key] * (-diff))

    return result


print("Task 4 Outputs:")
print(uncommon_elements([1,1,2], [2,3,4]))
print(uncommon_elements([1,2,3], [4,5,6]))
print(uncommon_elements([1,1,2,3,4,2], [1,3,4,5]))
