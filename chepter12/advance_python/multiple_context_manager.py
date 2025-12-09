# Multiple context managers in a single line
# r for read file and as f1 is used to assign the opened file object



with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    data1 = f1.read()
    data2 = f2.write(data1)   #length of data1 
print(data1,data2)

