# wap to print a table of 7 and show in vertical string of same number 
# when using string then use join method


table = [str (7*i) for i in range(1,11)]  # str because i want join then using str
print("\n" .join(table))

#or  using format method

table = ["7 x {} = {}".format(i, 7*i) for i in range(1, 11)]
print("\n".join(table))

# or using f string

table = [f"7 x {i} = {7*i}" for i in range(1, 11)]
print("\n".join(table))

#or using map
n = 7  # fixed number

def table_line(i):
    return f"{n} x {i} = {n * i}"

table = map(table_line, range(1, 11))
print("\n".join(table))

