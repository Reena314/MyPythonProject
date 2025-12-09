# wap to display a/b where a and b are ineger. if b==0 then display infinite by handling the zeroDivisionError

try:
    a= int(input("enter a number : "))
    b = int(input("enter second number :"))
    print ("division is : ", a/b)
    
except ZeroDivisionError:
    print("infinite")
    