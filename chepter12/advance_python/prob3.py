# wa list comperhension to print a list which contain the multiplication table enter a user number

num = int(input("enter a number : "))

mul_table = [num*i for i in range(1,11)]     # comperhension list 
print(mul_table)

#or 
num = int(input("Enter a number: "))

[print(f"{num} * {i} = {num * i}") for i in range(1, 11)]   #comperhension list



# or

num = int(input("Enter a number: "))

# List comprehension to generate the table values
mul_table = [num * i for i in range(1, 11)]       # comperhension list

# Print each multiplication in a formatted way
for i, val in enumerate(mul_table, start=1):
    print(f"{num} * {i} = {val}")
