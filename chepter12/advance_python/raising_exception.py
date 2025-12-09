
a = int(input("enter a number : "))
b = int(input("enter second number :"))

if (b == 0) :
    raise ZeroDivisionError("cannot divide by zero")  # raise is used to raise an exception for developer that solve the error 
else:
    print("division is : ", a/b)
