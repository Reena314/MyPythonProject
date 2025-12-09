''' wap to print a star pattern
  n = 3
  *
 ***
*****

'''

n = int(input("enter a number : ", ))
for  i in range (1, n+1):
    print(" "*(n-i), end="")     # end="" is used to print in same line and avoid new line
    print("*"*(2*i-1),end="")
    print("")

'''
*********
 *******
  *****
   *** 
    *
'''

n = int(input("enter a number :",))
for i in  range (n,0, -1):             #Start from i = n ,Go down to 1 , Step by -1 each time (counting backward)'''
    print(" " *(n-i), end="")       # here i starts with 5 and goes down to 1
    print("*"*(2*i-1), end="")
    print("")                         # new line like empty line


''' 

***
**
*

'''

n = int(input("enter a number :",))
for i in  range (n,0, -1):             #Start from i = n ,Go down to 1 , Step by -1 each time (counting backward)'''
    print(" " *(n-i), end="")
    print("*"*i, end="")
    print("")                         # new line like empty line


'''

* * *
*   *
* * *

'''
n = int(input("enter a number : "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*",end="")
        print(" "*(n-2), end= "")
        print("*" , end="")
    print(" ")








# '''

# ***
# **
# *

# '''
# n = int(input("enter a number : "))
# for i in range(n,0,-1):
#     print("*"*i , end= "")
#     print(" "*(n-i), end="")
#     print(""*i)