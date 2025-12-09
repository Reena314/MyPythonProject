# wap to print multiplication table of given number using for loop

num  =  int(input("enter a number : "))
for i in range(1,11):
    print(f"{num}*{i} = {num*i}")      # f string is used for formating string it means we can use variable in string.
    #They allow you to embed variables or expressions directly inside a string, using curly braces {}.



# with while loop same problem
n = int(input("enter a number : "))
i = 1
while(i<=10):
    print(f"{n}*{i} = {n*i}")
    i+= 1