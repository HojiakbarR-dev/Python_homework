# ===================================
# MAP and FILTER EXPLANATION + EXAMPLES
# ===================================

print("MAP and FILTER examples:\n")

# map() example – multiply each number by 2
nums = [1, 2, 3, 4]
mapped = list(map(lambda x: x * 2, nums))
print("map example (x*2):", mapped)

# filter() example – keep only even numbers
filtered = list(filter(lambda x: x % 2 == 0, nums))
print("filter example (even numbers):", filtered)

print("\n")


# ===================================
# 1. is_prime(n)
# ===================================
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print("is_prime results:")
print(is_prime(4))   # False
print(is_prime(7))   # True
print()


# ===================================
# 2. digit_sum(k)
# ===================================
def digit_sum(k):
    s = 0
    for digit in str(k):
        s += int(digit)
    return s

print("digit_sum results:")
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
print()


# ===================================
# 3. Powers of 2 up to N
# ===================================
def powers_of_two(N):
    p = 1
    result = []
    while p * 2 <= N:
        p = p * 2
        result.append(p)
    return result

print("Powers of 2 up to N:")
print(powers_of_two(10))   # [2, 4, 8]
print()


# ===================================
# (OLD HOMEWORK STARTS HERE)
# ===================================

# 1) Modify String with Underscores
def modify_with_underscores(s):
    vowels = set("aeiouAEIOU")
    res = []
    count = 0
    i = 0

    while i < len(s):
        res.append(s[i])
        count += 1

        if count == 3:
            pos = i
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

print("modify_with_underscores:")
print(modify_with_underscores("hello"))
print(modify_with_underscores("assalom"))
print(modify_with_underscores("abcabcabcdeabcdefabcdefg"))
print()


# 2) Integer squares
print("Integer squares:")
n = 5
for i in range(n):
    print(i * i)
print()


# 3) LOOP EXERCISES

# Exercise 1
print("Exercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2
print("Exercise 2:")
for r in range(1, 6):
    for c in range(1, r+1):
        print(c, end=" ")
    print()
print()

# Exercise 3
print("Exercise 3:")
n = 10
print("Sum is:", n * (n + 1) // 2)
print()

# Exercise 4
print("Exercise 4:")
num = 2
for i in range(1, 11):
    print(num * i)
print()

# Exercise 5
print("Exercise 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if 50 < n < 500 and n % 5 == 0 and n % 10 != 0:
        print(n)
print()

# Exercise 6
print("Exercise 6:")
num = "75869"
print(len(num))
print()

# Exercise 7
print("Exercise 7:")
n = 5
for start in range(n, 0, -1):
    for x in range(start, 0, -1):
        print(x, end=" ")
    print()
print()

# Exercise 8
print("Exercise 8:")
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])
print()

# Exercise 9
print("Exercise 9:")
for i in range(-10, 0):
    print(i)
print()

# Exercise 10
print("Exercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")
print()

# Exercise 11
print("Exercise 11:")
def is_prime2(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

for num in range(25, 51):
    if is_prime2(num):
        print(num)
print()

# Exercise 12
print("Exercise 12:")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# Exercise 13
print("Exercise 13:")
n = 5
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! =", fact)
print()


# 4) Uncommon elements
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    keys = set(c1.keys()) | set(c2.keys())
    for key in keys:
        diff = c1[key] - c2[key]
        if diff > 0:
            result.extend([key] * diff)
        elif diff < 0:
            result.extend([key] * (-diff))
    return result

print("uncommon_elements:")
print(uncommon_elements([1,1,2], [2,3,4]))
print(uncommon_elements([1,2,3], [4,5,6]))
print(uncommon_elements([1,1,2,3,4,2], [1,3,4,5]))
