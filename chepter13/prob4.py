# wap to filter a list of numbers which are divisible by 5

l = [1,2,3,4,5,6,7,8,9,10,15]

def div_by_5(num):
    if num%5 == 0:
        return True
    return False
only_div_by_5 = filter(div_by_5, l)
print(list(only_div_by_5))

#or

def divisible(n):
    if n%5 ==0:
        return True
    return False
a = 3456, 5,678,10,30
f = filter(divisible, a)
print(list(f))

# or using lambda
only_div_by_5 = filter(lambda x: x%5 == 0, l)
print(f'using lambda', list(only_div_by_5))

# or using map
only_div_by_5 = map(lambda x: x%5 == 0, l)
print(f'using map', list(only_div_by_5))

# or using reduce
# from functools import reduce                              # print error because reduce uses one parameters and if use reduce for division then use filter function
# only_div_by_5 = reduce(lambda x: x%5 == 0, l)
# print(f'using reduce',only_div_by_5)

l = [5, 10, 12, 15, 7, 20]

only_div_by_5 = list(filter(lambda x: x % 5 == 0, l))
print('Using filter:', only_div_by_5)


