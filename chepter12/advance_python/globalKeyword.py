# global keyword 

x = 10

def func():
    global x      # global keyword is used to modify the global variable if we not use global keyword then it will create a new local variable
    x = 20
    print(x)
func()
print(x)