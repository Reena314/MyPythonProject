# write a program to input eight numbers from the user and display unique numbers.

s = set()      # s means set and automatically sort the number

n = input("enter a number1 : ")
s.add(int(n))
n = input("enter a number2 : ")
s.add(int(n))
n = input("enter a number3 : ")
s.add(int(n))
n = input("enter a number4 : ")
s.add(int(n))
n = input("enter a number5 : ")
s.add(int(n))
n = input("enter a number6 : ")
s.add(int(n))
n = input("enter a number7 : ")
s.add(int(n))
n = input("enter a number8 : ")
s.add(int(n))
print(s)
