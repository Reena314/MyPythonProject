try:
    a = int(input("enter a number : "))
    print(a)                            # if no error then else block will execute
except Exception as e:
        print(e)
else:
    print("no error")


# another example

try:
    a = int(input("enter a number : "))
    b = int(input("enter second number : "))
    print("division is : ", a/b)           # if division success no error then else worked other wise exception work
except ZeroDivisionError as e:
    print("cannot divided by 0")
else:
    print("division successfull")

# now use finally
try:
    a = int(input("enter a number : "))
    b = int(input("enter second number : "))
    print("division is : ", a/b)
except ZeroDivisionError as e:
    print("cannot divided by 0")
except ValueError as e:
    print("enter valid number")
finally:                                  # always runs 
    print("This always runs, no matter what")

#now use try in files
try:
    with open("file1.txt", "r") as f1:     # if file not found then FileNotFoundError run and finally run
        f1.read()
except FileNotFoundError:
    print("file not found")
else: 
    print("file read successfully")
finally:
    print("finally block runs")
    

