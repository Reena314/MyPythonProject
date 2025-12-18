# check that a tuple number cannot be changed

a = ("karna", "banana", "kiwi")
a[1]="orange"
print(a)              # not changed because tuple is immutable

# x = list(a)
# print(x)
# x[1] = 'orange'           # we can change when tuple transfer to list
# print(x)