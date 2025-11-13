# %% [markdown]
# ### Task 1

# %%
year = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# %% [markdown]
# ### Task 2

# %%
number = int(input("Enter the number: "))

if number % 2 != 0:
    print("Weird")
elif number % 2 == 0 and 2 <= number <= 5:
    print("Not Weird")
elif number % 2 == 0 and 6 <= number <= 20:
    print("Weird")
elif number % 2 == 0 and number > 20:
    print("Not Weird")

# %% [markdown]
# ### Task 3

# %%
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# adjust start depending on whether a is even or odd
if a % 2 == 0:
    start = a
else:
    start = a + 1
evens = list(range(start, b + 1, 2))
print(evens)


# %%
a = int(input("Enter a: "))
b = int(input("Enter b: "))
evens = list(range(a + (a % 2), b + 1, 2))
print(evens)



