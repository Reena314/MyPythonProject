# wap to find the maximum number of the list using reduce

l = [1, 2,4, 55, 78, 6, 89, 345, 3,7]

from functools import reduce

def maximum(a,b):
    if a>b:
        return a 
    return b 

max = reduce(maximum, l)
print("maximum number is",max)

