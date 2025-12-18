# with statement

f = open("file.txt", "r")
data = f.read()
print(data)
f.close()       # if close file is not needed then we use with statement

#or

with open("file.txt","r") as f:
    print(f.read())
    
    # so with statement is used to close file automatically