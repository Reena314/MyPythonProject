fruits = ("mango", "green", 12, 34,456, "green")

print(fruits.count("green"))  #count


value = (1, 4, 8, 9,4, 3,8)
x = value.index(3)           #index
print(x)


my_tuple = (1,2,3,4)

myvalue = my_tuple*3     #repeated 3 times

print(myvalue)
print(2 in myvalue)


# tuples are unchageable or immutable But there are some workarounds.


x = ("apple", "banana", "cherry")
y = list(x)                         # first tuple convert in list and then changable or mutable
y[1] = "kiwi"
x = tuple(y)

print(x)


x1 = (1,2,3,5,6)
y1 =list(x1)
y1[3] = 4
x1 = tuple(y1)
print(x1)

#or
x1 = (1,2,3,5,6)
y1 =list(x1)
y1.append(7)
x1 = tuple(y1)
print(x1)
