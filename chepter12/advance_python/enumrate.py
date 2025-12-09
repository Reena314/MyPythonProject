#enumerate() is a built-in Python function that’s super useful when you’re looping through something (like a list) and you also need the index of each item.

l = [1,3,5,6,3,4,4]
index = 0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index +=1


    #or
for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")


