
'''a = int(input("enter the number : "))

print(a)       # print error but i want to print line enter the number so use try except'''

try:
    a = int(input("enter a number :", ))
    print(a)
except Exception as e:          # Exception is a base class for all exceptions and code not crash 
    print(e)
print("Thank you")

# if any problem in code then use exception if no problem then try block is continue



# ok now valueError

try :
    a = int(input("enter the number : "))
except ValueError as v:                 #  ValueError → correct type, invalid value and ValueError: invalid literal for int() with base 10
        print(v)
except Exception as e:
    print(e)
else:
    print("no error")



# another e.g
print("\n")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")


    