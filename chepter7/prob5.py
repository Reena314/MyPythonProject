#wap to calculate factorial of a given number

n =  int(input("enter a number : "))
factorial = 1
for  i in range(1, n+1):
    factorial = factorial * i     # f = 1x1 1x2 2x3 6x4 24x5     , 5x4x3x2x1
# print ("factorial number is  : ", factorial)
print(f"factorial of {n} is {factorial}")
