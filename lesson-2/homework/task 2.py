
# %%


# %% [markdown]
# ### Task1
# 

# %%
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

from datetime import date
cur_year = date.today().year

age = cur_year - birth_year

print(f"Hello {name}, your age is {age}")


# %% [markdown]
# ### Task 2

# %%
txt = "LMaasleitbtui"

car = txt[1] + txt[2] + txt[5] + txt[7] + txt[9] + txt[11]
car1 = car.capitalize()

print("Car name is:", car1)



# %% [markdown]
# ### Task 3
# 

# %%
txt = 'MsaatmiazD'

car2 = txt[0] + txt[2] +txt[4] + txt[6] +txt[8]
print("Car name is:", car2)

# %% [markdown]
# ### Task 4

# %%
txt = "I'am John. I am from London"
City = txt[21:]
print(City)

# %% [markdown]
# ### Task 5

# %%
input_string = str(input("Enter the string: "))

reversed_str = input_string[::-1]

print(reversed_str)


# %% [markdown]
# ### Task 6

# %%
input_string = input("Enter the string: ")

vowels = "aeiouAEIOU"
count = sum(input_string.count(char) for char in vowels)

print("Number of vowels:", count)


# %% [markdown]
# ### Task 7

# %%
numbers = input("Enter numbers: ")

num_list = [int(num) for num in numbers.split()]

max_value = max(num_list)

print("The maximum value is:", max_value)


# %% [markdown]
# ### Task 8
# 

# %%
word = str(input("Enter the word: "))
word.lower()
reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")

# %% [markdown]
# ### Task 9 

# %%
email = input("Enter you email: ")
at_symbol = email.find("@")

domain = email[at_symbol + 1:]

print("The domain of the email is:", domain)

# %% [markdown]
# ### Task 10 

# %%
import random
import string

letters = string.ascii_letters 
digits = string.digits         
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

all_chars = letters + digits + special_chars

length = int(input("Enter the password length: "))

password = "".join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)


# %%



