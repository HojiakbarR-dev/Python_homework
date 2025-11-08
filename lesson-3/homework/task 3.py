# %% [markdown]
# ### Task 1

# %%
fruit_list = ['olma', 'nok', 'uzum', 'banan', 'limon']

print(fruit_list[2])

# %% [markdown]
# ### Task 2
# 

# %%
list1 = [1, 2, 3]

list2 = [4, 5, 6]

combined_list = list1 + list2

print("Combined list:", combined_list)


# %% [markdown]
# ### Task 3

# %%
numbers = [10, 20, 30, 40, 50]

first = numbers[0]

middle_index = len(numbers) // 2  
middle = numbers[middle_index]

last = numbers[-1]

new_list = [first, middle, last]

print("New list with first, middle, and last elements:", new_list)


# %% [markdown]
# ### Task 4

# %%
movies_list = ['Inception', 'Interstellar', 'The Dark Knight', 'Forrest Gump', 'The Matrix']

movies_tuple = tuple(movies_list)

print("Movies as a tuple:", movies_tuple)


# %% [markdown]
# ### Task 5

# %%
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Berlin']

if 'Paris' in cities:
    print("Paris is in the list")
else:
    print("Paris is not in the list")

# %% [markdown]
# ### Task 6

# %%
numbers = [1, 2, 3, 4, 5]

duplicated_list = numbers * 2

print("Duplicated list:", duplicated_list)


# %% [markdown]
# ### Task 7

# %%
numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping:", numbers)




# %% [markdown]
# ### Task 8

# %%
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice_numbers = numbers[3:8]

print("Sliced tuple:", slice_numbers)


# %% [markdown]
# ### Task 9

# %%
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']

blue_count = colors.count('blue')

print("Number of times 'blue':", blue_count)


# %% [markdown]
# ### Task 10

# %%
animals = ('zebra', 'lion', 'tiger', 'elephant')
index_animal = animals.index('lion')

print("The index of 'lion' is ", index_animal)

# %% [markdown]
# ### Task 11

# %%
animals = ('zebra', 'lion', 'tiger', 'elephant')
cities = ('London', 'New York', 'Tokyo', 'Paris', 'Berlin')


Merged_tuple = animals + cities

print(Merged_tuple)

# %% [markdown]
# ### Task 12

# %%
animals = ('zebra', 'lion', 'tiger', 'elephant')    #tuple
cities = ['London', 'New York', 'Tokyo', 'Paris', 'Berlin']   #list

list_length = len(animals)
tuple_length = len(cities)

print(list_length)
print(tuple_length)

# %% [markdown]
# ### Task 13

# %%
numbers_tuple = (10, 20, 30, 40, 50)

# Convert the tuple to a list
numbers_list = list(numbers_tuple)

print("Converted list:", numbers_list)


# %% [markdown]
# ### Task 14

# %%
numbers = (10, 25, 5, 70, 30)

# Find maximum and minimum
max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)


# %% [markdown]
# ### Task 15

# %%
word_tuple = ('city', 'home', 'name', 'world')

reversed_tuple = word_tuple[::-1]

print(reversed_tuple)




