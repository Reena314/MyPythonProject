def myFunc():
    print("hello from module")
#    myFunc()                             # so same output in main.py file 

if __name__ == "__main__":               # if we run module.py directly then this block will run but if we   import this module in another file then this block will not run. so if __name__ == "__main__": is used to run the code only when the file is run directly and not when it is imported as a module.
    print("we are directly running this code")
    myFunc()