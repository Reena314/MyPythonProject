# write a program to input name marks and phonenumber of a student and format it using the format function

name = input("enter a name : ")
marks = int(input("enter marks of sub 1 :"))
phono = int(input("enter a phonenumber :"))

s = "my name is {} and my marks are {} and my phonenumber is {}" . format(name, marks, phono)
print(s)