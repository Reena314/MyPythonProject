# write a program to find the sum of first n natural numbers using recursion
'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(5) = 1+2+3+4+5
sum(n) = 1+2+3+4+5+.....(n -1) + n     # n-1 is before n 
'''


def sum(n):
    if n == 1  :
        return 1                      # base condition because if n == 1 then it will return 1
    else:
        return n+ sum(n-1)

print(sum(5))