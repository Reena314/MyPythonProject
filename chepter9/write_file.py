# write file

st = "hello python. i am learning python"
f = open("write.txt","w")
data = f.write(st)
print(data)
f.close()    #close file is important