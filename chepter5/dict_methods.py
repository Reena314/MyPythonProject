dict = {}  #empty dictionary

marks = {
    "karan" : 46,
    "kamal" :78,
    "frana" : 67,
     0 : 45
}

print(marks.items())
print(marks.values())
print(marks.keys())

marks.update({"frana": 99, "Renuka" :66})  #add renuka in list
print(marks)

print(marks.get("kamal")) # get marks
print(marks["kamal"]) # not same because of below


print(marks.get("kali")) # it perform none if user wrong
#print(marks["kali"]) # it perform error

dic_len = {"rahul": 30, "rohit": 40}
print(len(dic_len))
print(type(dic_len))

#       other methods from chatGpt


# my_dict = {'a': 1, 'b': 2, 'c': 3}

# print(my_dict.get('b'))           # 2
# print(my_dict.get('z', 0))        # 0 (default)

# print(my_dict.keys())             # dict_keys(['a', 'b', 'c'])
# print(my_dict.values())           # dict_values([1, 2, 3])
# print(my_dict.items())            # dict_items([('a', 1), ('b', 2), ('c', 3)])

# my_dict.update({'d': 4})
# print(my_dict)                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# my_dict.pop('a') 
# print(my_dict)                   # Removes key 'a'
# my_dict.popitem()                 # Removes the last item ('d': 4)

# new_dict = my_dict.copy()         # Shallow copy of dictionary
# print(new_dict) 
# default_val = my_dict.setdefault('e', 5)  # Inserts 'e': 5 if not present
# print(default_val)
# keys = ['x', 'y', 'z']
# empty_dict = dict.fromkeys(keys, 0)       # {'x': 0, 'y': 0, 'z': 0}
