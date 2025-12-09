list = ["black ", "green", 56,678.5, False, "akash"]

print(list)

print(list[3:5])

list.append("parneet")
print(list)

li = [1, 4, 45, 54, 67, 11]
li.sort()
print(li)
li.insert(3,4567)
print(li)
li.reverse()

print(li)
value = li.pop()
print(value)
print(li)
li.remove(45)
print(li)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

fruits1 = ["apple","banana","cherry"]
cars = ["tata", "bmw", "thar"]


fruits1.extend(cars)
print(fruits1)


fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry")
print(x)
