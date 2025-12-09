# if else condition

age = int(input("enter your age :"))

 # stmt one
if (age%2==0):
    print("your age is even")
# end of stmt one


# stmt two
if (age>=18):
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")

    print("your age is :",age)

# end of stmt two

  # elif else ladder
a = 20
b = 30
print("\n find greater numbers\n")

if (a<b):
    print("b is greater ")
elif(a>b):
    print("a is greater")
elif(a==b):
    print("a and b are equal")
else:
    print("a is greater")
   