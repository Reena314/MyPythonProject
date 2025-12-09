# wap to convert fahrenheit to celsius
# c/5 = f-32/9 or c = 5*(f-32)/9

def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(input("enter a number : "))
print("f to c is :", (f_to_c(f)))
#    or
c = f_to_c(f)
print(f"f to c is : {round(c,2)}")
    