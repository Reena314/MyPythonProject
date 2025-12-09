#wap to calculate factorial of a given number

n =  int(input("enter a number : "))
factorial = 1
for  i in range(1, n+1):
    factorial = factorial * i
# print ("factorial number is  : ", factorial)
print(f"factorial of {n} is {factorial}")