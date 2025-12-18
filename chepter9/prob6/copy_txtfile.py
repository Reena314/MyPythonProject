# wap to make a copy of text file "this.txt"

with open("this.txt","r") as f:
    txt = f.read()
    print(txt)

    with open("copy.txt", "w") as f:
        copy = f.write(txt)
        print(copy)