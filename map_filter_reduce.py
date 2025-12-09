# map() applies the function to all the items in an input_list.




l = [1,2,3,4,5]
square = lambda x : x*x
sqList = map(square, l)
print(list(sqList))

# in for loop
l = [1, 2, 3, 4, 5]
square = lambda x: x * x

sqList = []
for x in l:
    sqList.append(square(x))

print(sqList)

# in comperhension
l = [1, 2, 3, 4, 5]
sqList = [x * x for x in l]
print(sqList)

# using filter 

l = [1,2,3,4,5]

def even(n):
    if n%2 == 0:
        return True
    return False
onlyeven = filter(even, l)
print(list(onlyeven))


# reduce
from functools import reduce

l = [1, 2, 3, 4, 5]

def add(a, b):
    return a + b

total = reduce(add, l)   # 1+2=3, 3+3=6, 6+4=10, 10+5=15 and reduce(function, sequence)
# print(list(total))      # reduce return a single value not list
print(total)



