num1 = float(input("enter a number : "))
num2 = float(input("entaer second number : "))
print("\n choose operation :")
print("1 Addition  + ")
print("2 subtraction - ")
print("3 multiplication * ")
print("4 division /")

choice = input("enter your choice 1, 2, 3, 4 : ")

if choice == '1':
    print(num1+num2)
elif choice =="2":
    print(num1-num2)
elif choice == "3":
    print(num1*num2)
elif choice== "4" : 
    if num2 != 0:
     print(num1/num2)
    else:
       print("division by 0 not allowed")
else:
   print("invalid choice")


