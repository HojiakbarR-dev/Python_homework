# %% [markdown]
# ## Dictionary exercises

# %% [markdown]
# ### Task 1

# %%
data = {'a': 3, 'b': 1, 'c': 2}

sorted_items_asc = sorted(data.items(), key=lambda item: item[1])
sorted_dict_asc = dict(sorted_items_asc)
print("Ascending:", sorted_dict_asc)

sorted_items_desc = sorted(data.items(), key=lambda item: item[1], reverse=True)
sorted_dict_desc = dict(sorted_items_desc)
print("Descending:", sorted_dict_desc)


# %% [markdown]
# ### Task 2

# %%
d2 = {0: 10, 1: 20}
d2.update({2: 30})
print(d2)

# %% [markdown]
# ### Task 3

# %%
dict1 = {1: 10, 2: 11, 3: 12}
dict2 = {4: 13, 5: 14, 6: 15}
dict3 = {7: 16, 8: 17, 9: 18}

concatinated_dict = dict1 | dict2 | dict3
print(concatinated_dict)

# %% [markdown]
# ### Task 4

# %%
n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)


# %% [markdown]
# ### Task 5

# %%
squares_1_to_15 = {x: x*x for x in range(1, 16)}
print(squares_1_to_15)


# %% [markdown]
# ## Set Exercises

# %% [markdown]
# ### Task 1
# 

# %%
s = {1, 2, 3}
s.add(4)           # add single element
print(s)

# %% [markdown]
# ### Task 2

# %%
s.update([5, 6, 7]) # adds multiple elements
print(s)

# %% [markdown]
# ### Task 3

# %%
# update with another set
s.update({8, 9})
print(s)

# %% [markdown]
# ### Task 4
# 

# %%
elem = s.pop()
print("Removed:", elem, "remaining:", s)

# %% [markdown]
# ### Task 5

# %%
s = {1, 2, 3}


s.discard(2)   
print(s)


