# read file

f = open("file.txt", 'r')     # r is optional without r it will also work and r means read
data = f.read()
print(data)
f.close()