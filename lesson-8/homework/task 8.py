# %% [markdown]
# ### Python Exception Handling: Exercises, Solutions, and Practice
# 

# %%
#Task 1
try:
    numerator = float(input("Enter a numerator: "))
    denominator = float(input("Enter a denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")



# %%
#Task 2
try:
    number = int(input("Enter the number"))
    print(number)
except ValueError:
    print("Input is not valid integer")

# %%
#Task 3
file_name = input("Enter the file name: ")
try:
   with open(file_name, "r") as file:
      content = file.read()
      print("File is found", content)

except FileNotFoundError:
   print("File is not found")

# %%
#Task 4
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Function to check if input is numeric
def is_number(value):
    try:
        float(value)   # works for int, float, negative numbers
        return True
    except ValueError:
        return False

# Validate both inputs
if not (is_number(num1) and is_number(num2)):
    raise TypeError("Both inputs must be numerical.")

# Convert to float after validation
num1 = float(num1)
num2 = float(num2)

print("You entered:", num1, "and", num2)


# %%
# Task 5
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except PermissionError:
    print("Error: You do not have permission to open this file.")


# %%
# Task 6: IndexError handling
items = ["apple", "banana", "cherry"]

try:
    idx = int(input("Enter index to access (0-based): "))
    print("Item at index", idx, "is:", items[idx])
except IndexError:
    print("Error: Index out of range. Choose an index between 0 and", len(items)-1)
except ValueError:
    print("Error: Please enter a valid integer index.")


# %%
# Task 7: KeyboardInterrupt handling
try:
    value = input("Enter a number (press Ctrl+C to cancel): ")
    number = float(value)
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nInput cancelled by user (KeyboardInterrupt). Exiting gracefully.")
except ValueError:
    print("Error: That was not a valid number.")


# %%
# Task 8: ArithmeticError handling
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")
except ArithmeticError as ae:
    print("Arithmetic error occurred:", type(ae).__name__, "-", ae)
except ValueError:
    print("Error: Please enter valid numbers.")


# %%
# Task 9: UnicodeDecodeError handling
filename = input("Enter filename to read: ")

try:
    # attempt to open as text with UTF-8
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print("File content loaded successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except UnicodeDecodeError as ude:
    print("Error: Encoding/decoding problem while reading the file.")
    print("Details:", ude)
    # Option: show how to read in binary instead
    try:
        with open(filename, "rb") as f:
            raw = f.read()
        print("Read raw bytes (first 200 bytes):")
        print(raw[:200])
    except Exception as e:
        print("Also failed to read file in binary:", e)
except PermissionError:
    print("Error: Permission denied when trying to open the file.")


# %%
# Task 10: AttributeError handling
obj = (1, 2, 3)  # tuple doesn't have 'append'

try:
    # Trying to call an attribute that doesn't exist for this object
    obj.append(4)   # raises AttributeError
except AttributeError:
    print("Error: That object does not support the attribute/method you tried to use.")
    print("Example: tuple has no 'append'. Convert to list first if you need append.")
    # corrective example:
    fixed = list(obj)
    fixed.append(4)
    print("After converting to list, appended: ", fixed)


# %% [markdown]
# ### Python File Input Output: Exercises, Practice, Solution
# 

# %%
#Task 1
filename = "my_file.txt"
with open(filename, "r") as file:
    print(file.read())


# %%
#Task 2
filename = "my_file.txt"

n = int(input("Enter the line of text on the file: "))

with open(filename, "r") as file:
    for i in file:
        print(file.readline(), end="")

# %%
#Task 3 Append text to a file and display it
filename = "my_file.txt"

with open(filename, "a") as file: #Append text
    file.write("New line\n")

with open(filename, "r") as file:
    print(file.read())

# %%
#Task 4 
filename = "my_file.txt"

n = 2
with open(filename, "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line,  end="")

# %%
#Task 5
with open("my_file.txt", "r") as f:
    lines = f.readlines()

print(lines)


# %%
#Task 6
text = ""

with open("my_file.txt", "r") as f:
    for line in f:
        text += line

print(text)


# %%
#Task 7
arr = []

with open("my_file.txt", "r") as f:
    for line in f:
        arr.append(line.strip())

print(arr)


# %%
#Task 8
with open("my_file.txt", "r") as f:
    words = f.read().split()

max_len = len(max(words, key=len))

longest = [w for w in words if len(w) == max_len]

print(longest)


# %%
#Task 9

count = 0 # starting from zero

with open("my_file.txt", "r") as file:
    for lines in file:
        count+=1
print("Lines: ", count)

# %%
freq = {}

with open("my_file.txt", "r") as f:
    words = f.read().lower().replace(",", " ").split()

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)


# %%
import os

print(os.path.getsize("my_file.txt"), "bytes")


# %%
#12. Write a list to a file

data = ["apple", "banana", "cherry"]

with open("out.txt", "w") as f:
    for item in data:
        f.write(item + "\n")


# %%
#13. Copy contents of one file to another
with open("my_file.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)


# %%
#14 Combine each line from two files
with open("my_file.txt") as f1, open("copy.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip(), line2.strip())


# %%
# 15. Read a random line from a file
import random

with open("my_file.txt", "r") as f:
    lines = f.readlines()

print(random.choice(lines))


# %%
# 16. Check if file is closed
f = open("my_file.txt", "r")
print(f.closed)  # False
f.close()
print(f.closed)  # True


# %%
#17. Remove newline characters
with open("test.txt", "r") as f:
    lines = [line.strip() for line in f]

print(lines)

#18. Count words (comma separated too)
with open("test.txt", "r") as f:
    text = f.read().replace(",", " ")

words = text.split()

print("Word count:", len(words))

#19. Extract characters from files into a list
chars = []

for name in ["a.txt", "b.txt"]:
    with open(name, "r") as f:
        chars.extend(list(f.read()))

print(chars)

#20. Generate A.txt to Z.txt
import string

for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.write(letter)

 #21. Create a file with alphabet, N letters per line
import string

n = 5  # letters per line

letters = string.ascii_uppercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(letters[i:i+n] + "\n")


