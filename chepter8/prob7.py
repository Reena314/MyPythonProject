# wap to print multiplication table of given number using function

def table(n):
    for i in range(1, 11):
        print(f"{n}*{i} + {n * i}")

num = int(input("enter a number : "))
table(num)