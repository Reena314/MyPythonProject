'''
recursion is a function that calls itself

example of recursion
factorial of a number

factorial of 5 = 5 * 4 * 3 * 2 * 1
factorial of 4 = 4 * 3 * 2 * 1
factorial of 3 = 3 * 2 * 1
factorial of 2 = 2 * 1
factorial of 1 = 1
factorial of n = n * (n-1) * (n-2) * (n-3) * (n-4) * (n-5) * (n-6) * (n-7) * (n-8) * (n-9) * (n-10) * (n-11) * (n-12) * (n-13) * (n-14) * (n-15) * (n-16) * (n-17) * (n-18) * (n-19) * (n-20) * (n-21) * (n-22) * (n-23) * (n-24) * (n-25) * (n-26) * (n-27) * (n-28) * (n-29) * (n-30) * (n-31) * (n-32) * (n-33) * (n-34) * (n-35) * (n-36) * (n-37) * (n-38) * (n-39) * (n-40) * (n-41) * (n-42) * (n-43) * (n-44) * (n-45) * (n-46) * (n-47) * (n-48) * (n-49) * (n-50)


if i use n numbers then
factorial(n) = n * factorial(n-1) 

'''
num = int(input("enter a number : "))
def factorial(num):
    if(num == 1 or num ==0):
        return 1
    else:
        return num * factorial(num-1)          # recursive call or recursion    5 * 4x3x2x1
print(f"factorial of {num} is {factorial(num)}")




# Print numbers 1 to n using recursion

print("\n print numbers 1 to n using recursion")
def print_num(num):
    if(num == 0):            # base case
        return                 # it will return nothing   
    print_num(num-1)        #It does NOT print anything yet, it waits for the inner call to finish.
    print(num)             

print_num(5)                   

    