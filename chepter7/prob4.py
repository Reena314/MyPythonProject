# wap to find sum of first n natural numbers
num = int(input("enter a number : "))
i = 1
sum = 0
while(i<=num):
    sum = sum+i
    i+= 1
print("sum of first n natural number is :", sum)