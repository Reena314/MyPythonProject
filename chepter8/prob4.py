# write a python program print first n line of the pattern using function
'''
***
**
*
'''

def pattern(n):
    if (n==0):
        return           # base condition
    print("*"*n)                   
    pattern(n-1)                # recursive call

pattern(5)