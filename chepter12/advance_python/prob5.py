#wap to store multiplication table in a file name tables.txt
num = int(input("enter a number : "))
table = [num*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {num} : {str(table)}\n")