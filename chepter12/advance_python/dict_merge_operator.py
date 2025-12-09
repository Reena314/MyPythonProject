dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2  # merge dictionaries
print(merged)

# update dictionary
dict1 |= dict2         # update dictionary
print(dict1)


# merge and update with update
dict1.update(dict2)     # update dictionary
print(dict1)

