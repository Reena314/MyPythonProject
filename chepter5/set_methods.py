s1 = {1,2,3,4,5}
s2 = {4,6,8,9,3, 'karan'}

print(s1.union(s2))
print(s1|s2)         # union operator
print(s1.intersection(s2))
print(s1&s2)       # intersection operator

print(s1.difference(s2))      # in this common values are deleted and only s1 values shows
print(s1-s2)          # diffrence operator
print(s2-s1)          # remaing items  8 9 karan  6 and common deleted
print(sorted(s2 - s1, key=str)) 

s1.add(566)
print(s1)

print(type(s1))

print(len(s1))
s1.remove(566)
# s1.remove(10)      #error
s1.discard(10)       # no error its none
print(s1)

print(s1.clear())
